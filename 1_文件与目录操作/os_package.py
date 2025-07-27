# -*- coding: UTF-8 -*-
"""
    @Project : Item 
    @File    : os_package.py
    @Author  : XianZS
    @meaning : os 标准库学习
"""

import os

# 1. 获取当前的工作目录
current_dir = os.getcwd()
print(f"旧的-获取当前工作目录:{current_dir}")

# 2. 改变当前的工作目录
# os.chdir("E:/杂例/XianZS/Item/standard_library_python/")
current_dir = os.getcwd()
print(f"新的-获取当前工作目录:{current_dir}")

# 3. 创建目录(linux: mkdir 创建一个文件夹的意思)
# 相对路径
# os.mkdir("./This_is_my_make_dir")
# 绝对路径
os.mkdir("E:\\杂例\\XianZS\\Item\\standard_library_python\\1_文件与目录操作\\New_make")

print("---")
# 4. 删除目录 (linux:rm -rf 参数)
os.rmdir("./New_make")

# 5. 文件重命名和移动
# os.rename("./old.txt","./new.txt")
# os.rename("./new.txt", "../new_new.txt")

# 6. 删除文件
# os.remove("../new_new.txt")

# 7. 列出当前目录内容 >>> 列出子级目录和文件
files = os.listdir("../")
print(f"父级-当前目录内容:{files}")

# 8. 检查路径是否存在
if os.path.exists("./kkk"):
    print("路径存在")
else:
    print("路径不存在")

# 9. 运行系统命令
os.system("echo hello")
