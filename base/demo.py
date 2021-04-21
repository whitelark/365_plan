#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: BigC


# 斐波那契数列
# F(0) = 0、F(1) = 1、F(n) = F(n-1) + F(n-2)
a, b = 0, 1
while b < 100:
    print(b, end=",")
    a, b = b, a + b


# for语句可以遍历任何可迭代对象

