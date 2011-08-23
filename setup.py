#!/usr/bin/env python
"""
   Copyright 2006-2010 SpringSource (http://springsource.com), All Rights Reserved

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.       
"""
import re
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    try:
        from ez_setup import use_setuptools
    except ImportError:
        print "can't find ez_setup"
        print "try: wget http://peak.telecommunity.com/dist/ez_setup.py"
        sys.exit(1)
    use_setuptools()
    from setuptools import setup, find_packages

if sys.version_info < (2, 6):
    print "Spring Python only supports Python 2.6 and higher"
    sys.exit(1)


setup(name='springpython',
      version='1.2.0',
      description='Spring Python',
      long_description=open('README.txt').read(),
      author='Greg L. Turnquist',
      author_email='gturnquist at vmware dotcom',
      url='http://www.springpython.org',
      platforms = ["Python >= 2.6"],
      license='Apache Software License (http://www.apache.org/licenses/LICENSE-2.0)',
      #scripts=['src/plugins/coily'],
      package_dir = {'': 'src'},
      packages=find_packages('src'),
      package_data={'springpython': ["README", "COPYRIGHT", "LICENSE.txt"]},
      download_url="http://s3.amazonaws.com/dist.springframework.org/release/EXTPY/springpython-1.1.0.FINAL.tar.gz",
      classifiers=["License :: OSI Approved :: Apache Software License",
                   "Intended Audience :: Developers",
                   "Development Status :: 5 - Production/Stable",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   "Programming Language :: Python",
                   "Operating System :: OS Independent"
      ],
      install_requires=[
          'setuptools',
          'PyYAML'
      ]
)