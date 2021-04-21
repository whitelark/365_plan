#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: BigC

# 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表
# 列表切片语法格式：变量[start:end:step]

list_1 = "a b c d e f".split(" ")
list_1 = list_1[-1::-1]
output = " ".join(list_1)
print(output)  # f e d c b a


