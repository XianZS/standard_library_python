# -*- coding: UTF-8 -*-
"""
    @Project : Item 
    @File    : pathlib_package.py
    @Author  : XianZS
    @meaning : pathlib
"""
# 提供了一种面向对象的路径操作方式 >>> 比os.path()更强大
import pathlib

# 创建path对象
p = pathlib.Path("./obj.txt")
print(p, type(p))

# 先对文件对象p进行读取操作
p_things = p.read_text(encoding="utf-8")
print(p_things)
print("---")
# 对文件对象p进行写入操作 >>> 清空式写入操作
w_obj = "我是大帅哥"
p.write_text(w_obj, encoding="utf-8")
p_things = p.read_text(encoding="utf-8")
print(p_things)

# 删除文件
p.unlink()

"""
    我有一个目录，目录下面有好多文件
    我现在只想找出后缀为".py"的文件
    Path.cwd().glob("*.py")
"""

py_files = pathlib.Path.cwd().glob("*.py")
print(py_files)
for py_file in py_files:
    print(py_file)
