# -*- coding: utf-8 -*-
"""
    @Author  : weiyd
    @Contact : yitakabe@gmail.com
    @License : (C) Copyright 2020, Milink Corporation Limited.
    @Time    : 2020/11/4 18:12
    @FileName: module1.py
    @Desc    :
"""
# 系统模块
from unittest import TestCase

# 第三方模块

# 项目模块
from pack1 import module1_1


class TestFun(TestCase):
    def setup_class(self) -> None:
        print("\n类级别的setUpClass")

    def setUp(self) -> None:
        print("\n函数级别的setup")

    def test_fun(self):
        pass

    def test_fun2(self):
        assert module1_1.fun(10) == 100
        assert module1_1.fun(-10) == 100
        assert module1_1.fun(0) == 0

    def tearDown(self) -> None:
        print("\n函数级别tearDown")

    def teardown_class(self) -> None:
        print("类级别tearDownClass")


class TestFun2(TestCase):
    def test_fun(self):
        pass

    def test_fun2(self):
        assert module1_1.fun(10) == 100
        assert module1_1.fun(-10) == 100
        assert module1_1.fun(0) == 0
