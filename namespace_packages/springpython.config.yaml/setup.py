# import std
import os
from os import path
import sys
# import third party
# import local


if sys.version_info < (2, 6):
    print "Spring Python only supports Python 2.6 and higher"
    sys.exit(1)


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


# Append src directory to PYTHONPATH
sys.path.append(path.join(os.getcwd(), 'src'))
# Import metadata
from springpython.meta.springpython_config_yaml import __meta__

# Declare namespace packages
__namespace_packages__ = [
    'springpython',
    'springpython.config'
]

__package_data__ = [
    'README.rst',
    'Changelog',
    'License',
    'Makefile',
    'buildout.cfg'
]

__install_requires__ = [
    'setuptools',
    'PyYaml'
]


setup(
    name=__meta__['name'],
    version=__meta__['version_str'],
    description=__meta__['description'],
    long_description=open('README.rst').read(),
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='yaml config configuration springpython spring python applicationcontext application context',
    author=__meta__['author'],
    author_email=__meta__['author_email'],
    url=__meta__['url'],
    download_url='',
    license=__meta__['license'],
    namespace_packages = __namespace_packages__,
    package_dir = {'': 'src'},
    packages=find_packages('src', exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    package_data = {'': __package_data__},
    zip_safe=False,
    install_requires=__install_requires__,
    entry_points = {
        'console_scripts': [
        ]
    },
)
