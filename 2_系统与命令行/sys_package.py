# -*- coding: UTF-8 -*-
"""
    @Project : Item 
    @File    : sys_package.py
    @Author  : XianZS
    @meaning : sys 标准库讲解
"""

import sys

# 1. 获取命令行参数
datas = sys.argv
print(datas, type(datas))
print("-" * 10)
# 2. 模块的搜索路径 --- 将路径添加到环境遍历之中
datas = sys.path  # 环境变量
for data in datas:
    print(data)
print(type(datas))
print("=" * 10)
sys.path.append("E:\\杂例\\XianZS\\Item\\error-page")
datas = sys.path  # 环境变量
for data in datas:
    print(data)
print(type(datas))
print("*" * 10)
# 3. 输入和输出
# 读取键盘输入方式1：input()
# 读取键盘输入方式2：sys.stdin.readline()
sys.stdout.write("请输入一段话:")
sys.stdout.flush()
strs = sys.stdin.readline()
print(strs)
print(strs.strip())
