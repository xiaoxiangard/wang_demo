# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
import pytest


@pytest.mark.parametrize('name', ['�������', '�������'])
def test_code(name):
    print(f"name: {name}")