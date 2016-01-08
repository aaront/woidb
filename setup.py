#!/usr/bin/env python

import re
import ast

from codecs import open

from setuptools import setup, find_packages

requires = []

_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('woidb/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='woidb',
    version=version,
    description='A relational DB wrapper around data from war-on-ice.com data',
    long_description=open('README.rst', 'r', 'utf-8').read(),
    author='Aaron Toth',
    author_email='ajtoth@acm.org',
    url='http://github.com/aaront/woidb',
    include_package_data=True,
    packages=find_packages(),
    install_requires=requires,
    package_data={'': ['LICENSE']},
    package_dir={'woidb': 'woidb'},
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    )
)