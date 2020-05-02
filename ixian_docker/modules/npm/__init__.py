class NPMModuleConfig(object):
    """Custom config object for NPM module.

    Custom config to enable dynamically generated `dev_volumes`
    """

    name = "NPM"
    tasks = "ixian_docker.modules.npm.tasks"
    config = "ixian_docker.modules.npm.config.NPMConfig"
    dockerfile_template = "{NPM.DOCKERFILE_TEMPLATE}"

    def __getitem__(self, key):
        try:
            return getattr(self, key)
        except AttributeError:
            if key == "dev_volumes":
                return self.dev_volumes
            else:
                raise KeyError(key)

    def __contains__(self, key):
        return key in self.__dict__ or key == "dev_volumes"

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    @property
    def dev_volumes(self):
        from ixian_docker.modules.npm.utils import npm_local_package_mount_flags

        return npm_local_package_mount_flags()


OPTIONS = NPMModuleConfig()