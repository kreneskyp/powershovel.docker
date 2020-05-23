# Copyright [2018-2020] Peter Krenesky
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ixian.config import Config


class BlackConfig(Config):
    """Configuration for the **Black** module."""

    #: Config file used for **black**.
    #:
    #: ``pyproject.toml`` is also used by other components besides **black**
    CONFIG: str = "{DOCKER.APP_DIR}/etc/runtime/pyproject.toml"

    #: Source root that will be checked with black
    SRC: str = "{PYTHON.ROOT_MODULE_PATH}"

    #: Global args to passed to all calls to **black**.
    ARGS: str = ["--config {BLACK.CONFIG}", "{BLACK.SRC}"]


BLACK_CONFIG = BlackConfig()
