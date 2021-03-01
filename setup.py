#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="snapshot",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'snapshot = snapshot.script:begin', ],
    },
    version="1",
    author="Andrei Hryshkin",
    author_email="andrei_hryshkin@epam.com",
    description="App for logging the system",
    license="MIT"
)
