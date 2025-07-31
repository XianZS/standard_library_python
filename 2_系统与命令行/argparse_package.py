# -*- coding: UTF-8 -*-
"""
    @Project : Item 
    @File    : argparse_package.py
    @Author  : XianZS
    @meaning : argparse 标准库学习
"""

# 解析命令行参数 --- 深度学习领域
import argparse

# 创建 argparse 解析器
arg = argparse.ArgumentParser(description="argparse_package")

# 1. 必选参数设置
# arg.add_argument("rdd_count:", help="rdd算子个数")
# arg.add_argument("node:", help="分布式集群节点个数")
#
# print(arg.parse_args())

# 2. 可选参数设置 - 或 -- 开头
# arg.add_argument("-version", help="version things")
# arg.add_argument("-mode", help="mode things")
# print(arg.parse_args())

# 3. 参数类型设置
arg.add_argument("--number", type=int, help="input number")
arg.add_argument("--name", type=str, help="input name")
print(arg.parse_args())

# 4. 默认参数值设置 node=3
# arg.add_argument("--count", type=int, help="number count", default=3)
# print(arg.parse_args())

# 5. 互斥参数组
"""
mode1 互斥参数组
mode2 
组间内元素互斥
"""
# mode_group = arg.add_mutually_exclusive_group()
# mode_group.add_argument("--mode1", action="store_true")
# mode_group.add_argument("--mode2", action="store_true")

# 6. 枚举值设置
# arg.add_argument("--color", help="颜色参数设置",choices=["red","blue","white"])

# 7. 计数参数设置
arg.add_argument("-c", action="count", help="计数参数")

print(arg.parse_args())
