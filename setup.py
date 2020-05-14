#!/usr/bin/env python3
from setuptools import setup, find_namespace_packages

setup(
    name="rewebs",
    version="1.0",
    description="A simple python webdev server which also starts chromium and reloads the page on file change.",
    author="Thomas Rometsch",
    author_email="thomas.rometsch@uni-tuebingen.de",
    url="https://github.com/rometsch/rewebs",
    package_dir={'': 'src'},
    packages=find_namespace_packages(where="src"),
    install_requires=[
        "websockets",
        "websocket-client",
        "pyinotify"
    ],
    zip_safe=False,
    entry_points = {
        'console_scripts': ['rewebs=rewebs.main:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: Unix",
        "Topic :: Utilities"
    ],
    python_requires='>=3.6',
)
