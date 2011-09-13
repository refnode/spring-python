# Copyright 2006-2011, SpringSource - http://springsource.com
# All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


__all__ = ['__meta__']

# import std
# import third party
# import local


__version__ = (0, 1)
__version_str__ = '.'.join(map(str, __version__))

__meta__ = {
    'name': 'springpython.config.yaml',
    'author': 'Greg L. Turnquist',
    'author_email': 'gturnquist at vmware dotcom',
    'version': __version__,
    'version_str': __version_str__,
    'description': 'Yaml configuration format for SpringPython ApplicationContext',
    'url': 'http://www.springpython.org',
    'license': 'Apache Software License (http://www.apache.org/licenses/LICENSE-2.0)'
}