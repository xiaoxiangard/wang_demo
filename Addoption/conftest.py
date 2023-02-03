# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
import pytest
import yaml


# 定义一个命令行参数
def pytest_addoption(
        parser: "Parser", pluginmanager: "PytestPluginManager") -> None:
    mygroup = parser.getgroup("wxxgroup")  # group将下面所有的option都展示在这个group下面
    mygroup.addoption(
        "--env",  # 注册一个命令行选项
        default="test",  # 参数的默认值
        dest="env",  # 存储的变量，为属性命令，可以使用option对象访问这个值，暂时用不到
        help="set your run env"  # 帮助提示参数的描述信息
    )


# 针对传入不同的参数完成不同的处理逻辑
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
