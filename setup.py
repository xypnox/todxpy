# -*- coding: utf-8 -*- 
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="todx",
    version="0.1.3",
    author="xypnox",
    author_email="xypnox@gmail.com",
    description="A simple todo application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xypnox/todxpy",
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': ['todx=todx.main:main_command'],
    },
    install_requires = ['appdirs', 'fuzzywuzzy[speedup]'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
)
