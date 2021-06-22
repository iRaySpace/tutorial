# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in tutorial/__init__.py
from tutorial import __version__ as version

setup(
	name='tutorial',
	version=version,
	description='Tutorial',
	author='Ivan Ray Altomera',
	author_email='irayspacii@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
