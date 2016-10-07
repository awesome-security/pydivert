#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2016  Fabio Falcinelli
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import os

import pydivert
from setuptools import setup, find_packages

__author__ = 'fabio'

workdir = os.path.abspath(os.path.dirname(__file__))

setup(
    name='pydivert',
    version=pydivert.__version__,
    description='Python binding to windivert driver',
    # long_description=readme.read(),
    author='Fabio Falcinelli',
    author_email='fabio.falcinelli@gmail.com',
    url='https://github.com/ffalcinelli/pydivert',
    download_url='https://github.com/ffalcinelli/pydivert/tarball/{}'.format(pydivert.__version__),
    keywords=['windivert', 'network', 'tcp/ip'],
    license="LICENSE",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Operating System :: Microsoft :: Windows :: Windows Vista',
        'Operating System :: Microsoft :: Windows :: Windows Server 2008',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking :: Firewalls',
        'Topic :: System :: Networking :: Monitoring',
        'Topic :: Utilities',
    ],
    extras_require={
        "test": [
            "mock>=1.0.1",
            "pytest>=3.0.3",
            "pytest-cov>=2.2.1",
            "pytest-timeout>=1.0.0, <2",
            "pytest-faulthandler>=1.3.0, <2",
            "codecov>=2.0.5",
            "wheel>=0.29",
        ],
        # Do not use a range operator here: https://bitbucket.org/pypa/setuptools/issues/380
        # Ubuntu Trusty and other still ship with setuptools < 17.1
        ':python_version == "2.7"': [
            "win_inet_pton >= 1.0.1"  # available on 3.4+
        ],
        ':python_version == "3.3"': [
            "win_inet_pton >= 1.0.1"  # available on 3.4+
        ],
    }
)
