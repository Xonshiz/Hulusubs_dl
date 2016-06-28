#!/usr/bin/env python

from distutils.core import setup

setup(name='Distutils',
      version='2.0',
      description='Little Python Script To Download Susb from HULU.',
      author='Xonshiz',
      author_email='Xonshiz@psychoticelites.com',
      url='https://github.com/Xonshiz/Hulu-Subs-Downloader',
      install_requires=['lxml','bs4','requests','re','os','sys']
     )