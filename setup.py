#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages
import os
import shutil

for name in ['dist', 'build']:
    dist_path = os.path.join(os.path.dirname(__file__), name)
    if os.path.exists(dist_path):
        shutil.rmtree(dist_path)
setup(
    name='pmgwidgets',
    version='0.9.4',
    description=(
            'A Widget Collection for PyMiner Project. Especially for creating forms by simple jsons.\n' +
            'This package is developed by PyMiner developing team.'
    ),
    author='hzy15610046011',
    author_email='1295752786@qq.com',
    license='LGPL',
    packages=find_packages(),
    platforms=["all"],
    url='https://gitee.com/hzy15610046011/pyminer_comm',
    install_requires=[
        'qtpy',
        'chardet'
    ],
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries'
    ],
    include_package_data=True
)
