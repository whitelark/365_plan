#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: BigC


# 迭代器
# 迭代器是一个可以记住遍历位置的对象
# 迭代器有两个基本方法iter()和next()
list_1 = [1, 2, 3, 4]

# 创建迭代器对象
it = iter(list_1)
# 输出迭代器的下一个元素
# num = next(it)
# print(num)

# 迭代器对象可以使用常规for语句进行遍历
for i in it:
    print(i)

# 把一个类作为一个迭代器使用需要在类中实现两个方法__iter()__、__next()__


# 生成器
# 在 Python 中，使用了 yield 的函数被称为生成器（generator）
# 与普通函数不同，生成器是一个返回迭代器的函数，只能用于迭代操作
# 调用生成器运行的过程中，每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值，并在下一次执行next()方法时从当前位置继续运行




