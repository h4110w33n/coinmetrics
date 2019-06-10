#!/usr/bin/env python3
"""
Setup for Coin Metrics API.
"""

from setuptools import setup

setup(
	name='Coin Metrics API',
	version='1.0.0',
	author="Robert Rice",
	author_email="h4110w33n@gmail.com",
	url='',
	description='',
	long_description='',
	keywords=['coinmetrics', 'crypto', 'cryptocurrency', 'rest', 'api'],
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'Intended Audience :: End Users/Desktop',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: POSIX :: Linux',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python',
	],
	requires=['requests'],
	install_requires=['requests'],
	provides=['nielsen'],
	entry_points={
		'console_scripts': ['coinmetrics=bin.cli:main'],
	},
	platforms='linux',
	license='GNU General Public License v3 (GPLv3)',
	packages=['coinmetrics'],
)