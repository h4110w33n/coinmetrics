#!/usr/bin/env python3
"""
Setup for Coin Metrics API.
"""

from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
	name='Coin Metrics API for Python',
	version='0.1.0',
	author="Robert Rice",
	author_email="h4110w33n@gmail.com",
	url='https://github.com/h4110w33n/coinmetrics',
	description='An unofficial library to standardize queries to the Coin Metrics (coinmetrics.io) API.',
	long_description='An unofficial library to standardize queries to the Coin Metrics (coinmetrics.io) API.',
	keywords=['coinmetrics', 'crypto', 'cryptocurrency', 'rest', 'api'],
	classifiers=[
		'Development Status :: 4 - Beta ',
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
		'Topic :: Scientific/Engineering :: Mathematics'
		'Topic :: Software Development :: Libraries :: Python Modules',
	],
	requires=requirements,
	install_requires=requirements,
	provides=['coinmetrics'],
	license='GNU General Public License v3 (GPLv3)',
	packages=['coinmetrics'],
)
