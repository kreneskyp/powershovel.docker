from power_shovel.task import task
from power_shovel_docker.modules.docker.tasks import compose


def python_local_package_mount_flags():
    return []


@task()
def pipenv(*args):
    """
    Run a pipenv command.

    This runs in the builder container with volumes mounted.
    """
    compose('pipenv', *args)


@task()
def build_pip(*args):
    """Run pipenv install"""
    compose('pipenv install', *args)