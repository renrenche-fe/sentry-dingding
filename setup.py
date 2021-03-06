#!/usr/bin/env python
# encoding=utf-8

"""
rrc-sentry-dingding-robot
==============
sentry 钉钉机器人通知插件
"""
from setuptools import setup, find_packages

install_requires = [
    'sentry>=6.0.0',
]

setup(
    name='rrc-sentry-dingding-robot',
    version='1.2.3',
    author='xierenhong',
    author_email='xierenhong@renrenche.com',
    url='https://github.com/renrenche-fe/sentry-dingding',
    description='Sentry的钉钉插件',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    entry_points={
        'sentry.apps': [
            'sentry_dingding = sentry_dingding',
        ],
        'sentry.plugins': [
            'dingding = sentry_dingding.models:DingDingMessage',
         ],
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
