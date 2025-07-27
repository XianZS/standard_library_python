# -*- coding: UTF-8 -*-
"""
    @Project : Item 
    @File    : glob_package.py
    @Author  : XianZS
    @meaning : glob 标准库学习
"""
# 文件名模式匹配
import glob

py_files = glob.glob("**/*.py", recursive=True)
print(py_files, type(py_files))

# 匹配文件名以"my"开头，并且后缀为csv的文件 >>> re标准库 正则表达式
files = glob.glob("my*.csv")
print(files, type(files))
