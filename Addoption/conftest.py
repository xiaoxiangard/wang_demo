# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
import pytest
import yaml


# ����һ�������в���
def pytest_addoption(
        parser: "Parser", pluginmanager: "PytestPluginManager") -> None:
    mygroup = parser.getgroup("wxxgroup")  # group���������е�option��չʾ�����group����
    mygroup.addoption(
        "--env",  # ע��һ��������ѡ��
        default="test",  # ������Ĭ��ֵ
        dest="env",  # �洢�ı�����Ϊ�����������ʹ��option����������ֵ����ʱ�ò���
        help="set your run env"  # ������ʾ������������Ϣ
    )


# ��Դ��벻ͬ�Ĳ�����ɲ�ͬ�Ĵ����߼�
@pytest.fixture(scope="session")
def cmdoption(request):
    myenv = request.config.getoption("--env", default="test")
    if myenv == "test":
        datapath = "test/data.yml"
    else:
        datapath = "dev/data.yml"

    with open(datapath) as f:
        datas = yaml.safe_load(f)
    return myenv, datas
