# -*- coding: utf8 -*-
#
# This file were created by Python Boilerplate. Use Python Boilerplate to start
# simple, usable and best-practices compliant Python projects.
#
# Learn more about it at: http://github.com/fabiommendes/python-boilerplate/

"""
Still working on this -Adrian
"""

import os

from setuptools import setup, find_packages

# Meta information
version = open('VERSION').read().strip()
dirname = os.path.dirname(__file__)

# Save version and author to __meta__.py
path = os.path.join(dirname, 'src', 'python_boilerplate', '__meta__.py')
data = '''# Automatically created. Please do not edit.
__version__ = u'%s'
__author__ = u'F\\xe1bio Mac\\xeado Mendes'
''' % version
with open(path, 'wb') as F:
    F.write(data.encode())
    
setup(
    # Basic info
    name='overlay',
    version=version,
    author='aidswidjaja',
    author_email='noreply@adrian.id.au',
    url='https://github.com/aidswidjaja/fugai',
    description='Cross-platform and open-source overlay for rapid communication and information with minimal performance impact for macOS and Linux and maybe Windows.',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],

    # Packages and depencies
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'jinja2',
        'invoke>=0.13',
        'unidecode',
        'six',
        'pygobject3',
        'pycairo',
    ],
    extras_require={
        'dev': [
            'manuel',
            'pytest',
            'pytest-cov',
            'coverage',
            'mock',
        ],
    },

    # Data files
    package_data={
        'python_boilerplate': [
            'templates/*.*',
            'templates/license/*.*',
            'templates/docs/*.*',
            'templates/package/*.*'
        ],
    },

    # Scripts
    entry_points={
        'console_scripts': [
            'python-boilerplate = python_boilerplate.__main__:main'],
    },

    # Other configurations
    zip_safe=False,
    platforms='any',
)
