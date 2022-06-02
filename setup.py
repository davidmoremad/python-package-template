# -*- coding: utf-8 -*-
# Copyright (C) 2022 David Amrani Hernandez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import io
from setuptools import setup, find_packages
from package import __author__, __license__, APP_NAME, APP_DESCRIPTION

def read_file(filename):
    with io.open(filename, encoding='utf-8') as f:
        return f.read()

REPOSITORY_URL = 'https://github.com/davidmoremad/myrepo'
AUTHOR_EMAIL = 'davidmorenomad@gmail.com'

setup(
    name=APP_NAME,
    version=read_file('VERSION').strip(),
    install_requires=read_file('requirements.txt').splitlines(),
    packages=find_packages(),
    author=__author__,
    author_email=AUTHOR_EMAIL,
    url=f'{REPOSITORY_URL}',
    project_urls={
        'Documentation': f'{REPOSITORY_URL}/blob/master/README.md',
        'Source Code': f'{REPOSITORY_URL}',
        'Bug Tracker': f'{REPOSITORY_URL}/issues',
        'Download': f'https://pypi.org/project/{APP_NAME}/#files'
    },
    description=APP_DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=read_file('README.md'),
    keywords='tag1 tag2 tag3',
    license=__license__,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Security',
        'Topic :: Software Development',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    # Console_scripts creates a binary to run on the command line
    entry_points = {
        'console_scripts': [
            'app-cli = package.script:run',
        ],
    },
)
