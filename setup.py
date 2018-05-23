#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# regex2grok
# Create by askeing_yen on 23/05/2018

from setuptools import setup, find_packages

DEFAULT_REQUIREMENT = "requirements.txt"

with open(DEFAULT_REQUIREMENT) as f:
    deps = f.read().splitlines()

version = "0.0.1"

# main setup script
setup(
    name="regex2grok",
    version=version,
    description="Simplify the steps from regex to grok format.",
    author="Askeing Yen",
    author_email="askeing@gmail.com",
    url='https://github.com/askeing/regex2grok',
    install_requires=deps,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
    entry_points="""
    # -*- Entry points: -*-
    [console_scripts]
    regex2grok = regex2grok.regex2grok:main
    """,
)
