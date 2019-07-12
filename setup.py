# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name='radicale_storage_etesync',
    version='0.10.0',
    author='EteSync',
    author_email='development@etesync.com',
    url='https://github.com/etesync/radicale_storage_etesync',
    description='DEPRECATED: merged into etesync-dav',
    keywords=['etesync', 'encryption', 'sync', 'pim', 'radicale'],
    license='GPL',
    long_description=open('DESCRIPTION.rst').read(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'etesync-dav',
    ]
)
