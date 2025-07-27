# -*- coding: UTF-8 -*-
"""
    @Project : Item 
    @File    : shutil_package.py
    @Author  : XianZS
    @meaning : shutil 标准库学习
"""

import shutil

# 1. 复制文件
shutil.copy("./my_src.txt", "my_src_copy.txt")

# # 2. 复制目录 >>> 顺便复制目录中的文件
shutil.copytree("./my_src", "my_src_copy")
#
# # 3. 移动文件到某个目录 传入参数(文件,将要抵达的路径)
shutil.move("./my_src_copy.txt", "./my_src_copy/")

print("---")
# 4. 删除目录 非空目录 目录存在
shutil.rmtree("./my_src_copy")
