# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from pysnap import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestNPMConfig.test_read[DOCKERFILE] 1'] = '/home/runner/work/ixian-docker/ixian-docker/ixian_docker/modules/npm/Dockerfile'

snapshots['TestNPMConfig.test_read[IMAGE] 1'] = 'docker.io/library/unittests:npm-a7bfe49896774c216dc7321cc98597cce1dbbf5d0da2592368b82139dbf3bdd5'

snapshots['TestNPMConfig.test_read[IMAGE_TAG] 1'] = 'npm-a7bfe49896774c216dc7321cc98597cce1dbbf5d0da2592368b82139dbf3bdd5'

snapshots['TestNPMConfig.test_read[MODULE_DIR] 1'] = '/home/runner/work/ixian-docker/ixian-docker/ixian_docker/modules/npm'

snapshots['TestNPMConfig.test_read[NODE_MODULES_DIR] 1'] = '/opt/unittests/node_modules'

snapshots['TestNPMConfig.test_read[PACKAGE_JSON] 1'] = 'package.json'

snapshots['TestNPMConfig.test_read[REPOSITORY] 1'] = 'docker.io/library/unittests'

snapshots['TestNPMConfig.test_read[BIN] 1'] = '/opt/unittests/node_modules/.bin'

snapshots['TestNPMConfig.test_read[IMAGE_FILES] 1'] = [
    '{PWD}/root/srv/etc/npm/'
]

snapshots['TestNPMConfig.test_read[VOLUME] 1'] = 'npm-a7bfe49896774c216dc7321cc98597cce1dbbf5d0da2592368b82139dbf3bdd5'

snapshots['TestNPMConfig.test_task_hash 1'] = GenericRepr('<ixian.config.TaskConfig object at 0x100000000>')
