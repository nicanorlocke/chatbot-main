#!/usr/bin/python3
# Copyright 2024 AIR Institute
# See LICENSE for details.
# Author: AIR Institute (@tobeal on GitHub)


import io
from setuptools import setup, find_packages


def readme():
    with io.open('README.md', encoding='utf-8') as f:
        return f.read()


def requirements(filename):
    reqs = list()
    with io.open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            yield line.strip()


setup(
    name='chatbot_api',
    version='1.0',
    packages=find_packages(),
    url="https://github.com/bisite/project",
    download_url='https://github.com/bisite/project/archive/1.0.tar.gz',
    license='LICENSE.md',
    author='AIR Institute',
    author_email='amontero@air-institute.com',
    description='',
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=requirements(filename='requirements.txt'),
    data_files=[],
    entry_points={
        'console_scripts': [
            'chatbot_api=chatbot_api.run:main'
        ],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers"
    ],
    python_requires='>=3',
    project_urls={
        'Bug Reports': 'https://github.com/bisite/project/issues',
        'Source': 'https://github.com/bisite/project'
    },
)