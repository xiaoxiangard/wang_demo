# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
from setuptools import setup, find_packages
setup(
    name='Encode',
    url='git@github.com:xiaoxiangard/wang_demo.git',
    version='1.0',
    author="wangxiaoxiang",
    author_email='526420380@qq.com',
    description='set your encoding and logger',
    long_description='Show Chinese for your mark.parametrize(). Define logger variable for getting your log',
    classifiers=[
        # 分类索引 ，pip 对所属包的分类
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.8',
    ],
    license='proprietary',
    packages=find_packages(),  # ['Encode'],
    keywords=[
        'pytest', 'py.test', 'encode_plugin',
    ],

    # 需要安装的依赖
    install_requires=[
        'pytest'
    ],
    # 入口模块 或者入口函数
    entry_points={
        'pytest11': [
            'Encode = Encode.encode_plugin',
        ]
    },
    zip_safe=False
)