#!/usr/bin/env python
# coding: utf-8

import sys
from setuptools import setup

if sys.version_info < (2, 7, 0) or (3, 0, 0) <= sys.version_info < (3, 4, 0):
    sys.stderr.write('ERROR: You need Python 2.7 or 3.4+ '
                     'to install the typing package.\n')
    exit(1)

version = '3.7.4.3'
description = 'Type Hints for Python'
long_description = '''\
Typing Extensions -- Backported and Experimental Type Hints for Python

The ``typing`` module was added to the standard library in Python 3.5, but
many new features have been added to the module since then.
This means users of Python 3.5 - 3.6 who are unable to upgrade will not be
able to take advantage of new types added to the ``typing`` module, such as
``typing.Protocol`` or ``typing.TypedDict``.

The ``typing_extensions`` module contains backports of these changes.
Experimental types that will eventually be added to the ``typing``
module are also included in ``typing_extensions``, such as
``typing.ParamSpec`` and ``typing.TypeGuard``.

Users of Python versions before 3.5 should install and use
the ``typing`` module from PyPI instead of using this one, unless specifically
writing code that must be compatible with multiple Python versions or requires
experimental types.
'''

classifiers = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Python Software Foundation License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Topic :: Software Development',
]

if sys.version_info.major == 2:
    package_dir = 'typing_extensions/src_py2'
elif sys.version_info.major == 3:
    package_dir = 'typing_extensions/src_py3'
else:
    raise AssertionError()

setup(name='typing_extensions',
      version=version,
      description=description,
      long_description=long_description,
      author='Guido van Rossum, Jukka Lehtosalo, Łukasz Langa, Michael Lee',
      author_email='levkivskyi@gmail.com',
      url='https://github.com/python/typing/blob/master/typing_extensions/README.rst',
      license='PSF',
      keywords='typing function annotations type hints hinting checking '
               'checker typehints typehinting typechecking backport',
      package_dir={'': package_dir},
      py_modules=['typing_extensions'],
      classifiers=classifiers)
