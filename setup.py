# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in it_manage/__init__.py
from it_manage import __version__ as version

setup(
	name='it_manage',
	version=version,
	description='It module',
	author='umis',
	author_email='teddy@umis.co.id',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
