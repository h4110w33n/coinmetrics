#!/usr/bin/env python3
"""
Setup for Coin Metrics API.
"""
import os
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
	name='coinmetrics',
	version='0.2.1',
	author="Robert Rice",
	author_email="h4110w33n@gmail.com",
	url='https://github.com/h4110w33n/coinmetrics',
	description='An unofficial library to standardize queries to the Coin Metrics (coinmetrics.io) API.',
	long_description='An unofficial library to standardize queries to the Coin Metrics (coinmetrics.io) API.',
	keywords=['coinmetrics', 'crypto', 'cryptocurrency', 'rest', 'api'],
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Intended Audience :: Education',
		'Intended Audience :: Financial and Insurance Industry',
		'Intended Audience :: Information Technology',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python',
		'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
		'Topic :: Scientific/Engineering :: Information Analysis',
		'Topic :: Scientific/Engineering :: Mathematics',
		'Topic :: Software Development :: Libraries :: Python Modules',
	],
	install_requires=required,
	provides=['coinmetrics'],
	license='GNU General Public License v3 (GPLv3)',
	packages=['coinmetrics'],
)
