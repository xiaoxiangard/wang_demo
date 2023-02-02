# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
import pytest


@pytest.mark.parametrize('name', ['插件开发', '开发插件'])
def test_code(name):
    print(f"name: {name}")