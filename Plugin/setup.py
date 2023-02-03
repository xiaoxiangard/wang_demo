# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
from setuptools import setup, find_packages
setup(
    name='encode_plugin',
    url='git@github.com:xiaoxiangard/wang_demo.git',
    version='1.0',
    author="wangxiaoxiang",
    author_email='526420380@qq.com',
    description='set your encoding and logger',
    long_description='Show Chinese for your mark.parametrize(). Define logger variable for getting your log',
    classifiers=[
        # �������� ��pip ���������ķ���
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.8',
    ],
    license='proprietary',
    packages=find_packages(),  # ['encode_plugin'],
    keywords=[
        'pytest', 'py.test', 'encode_plugin',
    ],

    # ��Ҫ��װ������
    install_requires=[
        'pytest'
    ],
    # ���ģ�� ������ں���
    entry_points={
        'pytest11': [
            'encode_plugin = Encode.encode_plugin',
        ]
    },
    zip_safe=False
)