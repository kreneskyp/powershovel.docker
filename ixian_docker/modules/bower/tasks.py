import docker
from ixian.task import Task
from ixian.config import CONFIG
from ixian.modules.filesystem.file_hash import FileHash
from ixian_docker.modules.docker.checker import (
    DockerVolumeExists,
    DockerImageExists,
)
from ixian_docker.modules.docker.tasks import run
from ixian_docker.modules.docker.utils.images import build_image_if_needed
from ixian_docker.modules.docker.utils.volumes import delete_volume

BOWER_DEPENDS = ["build_app_image"]


def clean_bower():
    """
    Remove bower volume
    """
    delete_volume(CONFIG.BOWER.COMPONENTS_VOLUME)


class BuildBowerImage(Task):
    name = "build_bower_image"
    parent = "build_image"
    depends = ["build_base_image"]
    category = "build"
    short_description = "Build bower image"
    check = [
        FileHash("{BOWER.DOCKERFILE}", *CONFIG.resolve("BOWER.IMAGE_FILES")),
        DockerImageExists("{BOWER.IMAGE}"),
    ]

    def execute(self, pull=False):
        build_image_if_needed(
            repository=CONFIG.BOWER.REPOSITORY,
            tag=CONFIG.BOWER.IMAGE_TAG,
            dockerfile=CONFIG.BOWER.DOCKERFILE,
            force=self.__task__.force,
            pull=pull,
            # recheck=self.check.check,
            buildargs={
                "FROM_REPOSITORY": CONFIG.DOCKER.REPOSITORY,
                "FROM_TAG": CONFIG.DOCKER.BASE_IMAGE_TAG,
            },
        )


class BuildBower(Task):
    """Install bower packages to the app container"""

    name = "build_bower"
    depends = BOWER_DEPENDS
    category = "build"
    short_description = "Install bower packages"
    #parent = "build_app"
    clean = clean_bower
    check = [
        FileHash("{BOWER.CONFIG_FILE}"),
        DockerVolumeExists("{BOWER.COMPONENTS_VOLUME}"),
    ]

    def execute(self, *args):
        run(
            "{BOWER.BIN} install {BOWER.CONFIG_FILE_PATH}",
            CONFIG.BOWER.ARGS + list(args),
        )


class Bower(Task):
    """
    Bower package manager.

    This task is a proxy to the bower package manager. It runs within the
    context of the app container. Changes made persist for local dev
    environments.

    For bower help type: ix bower --help
    """

    name = "bower"
    depends = BOWER_DEPENDS
    category = "libraries"
    short_description = "Bower package manager"
    clean = clean_bower

    def execute(self, *args):
        run("{BOWER.BIN}", CONFIG.BOWER.ARGS + list(args))