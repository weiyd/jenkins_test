# -*- coding: utf-8 -*-
"""
    @Author  : weiyd
    @Contact : yitakabe@gmail.com
    @License : (C) Copyright 2020, Milink Corporation Limited.
    @Time    : 2020/11/4 17:48
    @FileName: test_module1.py
    @Desc    :
"""
# 系统模块

# 第三方模块
import pytest
# 项目模块
from pack1 import module1_1


def test_module1_1_fun():  # test开头的测试函数
    assert module1_1.fun(10) == 100
    assert module1_1.fun(-10) == 100
    assert module1_1.fun(0) == 0


