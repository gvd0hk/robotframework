#  Copyright 2008 Nokia Siemens Networks Oyj
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import sys
import re

from robot.version import get_version


def get_java_version():
    if not sys.platform.startswith('java'):
        return (0, 0)
    try:
        res = re.match("java(\d+)\.(\d+)", sys.platform)
        if not res:
            raise ValueError
        return int(res.group(1)), int(res.group(2))
    except ValueError:
        raise EnvironmentError('Invalid Java version: %s' % sys.platform)
