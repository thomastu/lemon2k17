# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='lemon2k17',
    version='0.0.0',

    description='Terminal-based lemonade stand game in the spirit of the business tycoon sim from our childhoods.',
    long_description='',

    url='https://github.com/thomastu/lemon2k17',

    author='Thomas Tu, Brian Klein-Qiu, Ryan Higgins',
    author_email='',

    license='',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Bored Technical Staff',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='lemonade stand',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['future'],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage', 'nose'],
    },

    package_data={
    },

    entry_points={
        'console_scripts': [
            'lemon2k17=lemon2k17.scripts.console:main',
        ],
    },
)
