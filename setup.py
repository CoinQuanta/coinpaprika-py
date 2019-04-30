#!/usr/bin/env python3
"""coinpaprika-py setup"""

import sys
from codecs import open
from os import path
from setuptools import setup

__version__ = "1.0-a1"
PACKAGE_NAME = "coinpaprika"
HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
    README = f.read()

setup(name=PACKAGE_NAME,
      author="CoinQuanta",
      author_email="hello@coinquanta.com",
      description="Access Coinpaprika's API with ease using coinpaprika-py.",
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Topic :: Utilities",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "Operating System :: OS Independent",
          "Natural Language :: English",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: Implementation :: CPython"],
      install_requires=["requests>=2.20.0"],
      keywords="coinpaprika crypto cryptocurrency api",
      long_description=README,
      license="MIT",
      url="https://github.com/CoinQuanta/coinpaprika-py",
      packages=["coinpaprika"],
      version=__version__)
#  vim: set ts=4 sw=4 tw=79 ft=python et :
