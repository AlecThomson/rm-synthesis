#!/usr/bin/env python

from distutils.core import setup

setup(name='RM synthesis',
      version='0.4',
      description='Simple Faraday rotation measure synthesis tool',
      author='Michiel Brentjens',
      author_email='brentjens@astron.nl',
      url='',
      packages=['rmsynthesis'],
      scripts=['bin/rmsynthesis'],
     )
