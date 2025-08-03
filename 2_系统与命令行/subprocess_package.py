# -*- coding: UTF-8 -*-
"""
    @Project : Item 
    @File    : subprocess_package.py
    @Author  : XianZS
    @meaning : 
"""
import subprocess
import time

# 创建和进行子进程管理
# * 阻塞式进程
# * 非阻塞式进程
""" 阻塞式进程的使用 """
# res1 = subprocess.run(["echo", "hello world"],
#                       shell=True)
# print(f"res1:{res1}")
# print("===")
""" 非阻塞式进程的使用 """
# res = subprocess.Popen(["echo", "hello world"], shell=True)
# print(f"res:{res}")
# # 捕捉输出流
# proc = subprocess.Popen(["echo", "hello world"],
#                         stdout=subprocess.PIPE,
#                         text=True,
#                         shell=True)
# output, _ = proc.communicate()
# print(f"output:{output}")
# subprocess 进行进程的后台管理
proc = subprocess.Popen(["python", "-m", "http.server", "8000"], shell=True)
for x in range(3):
    print(f"休眠第{x + 1}秒")
    time.sleep(1)

proc.terminate()

# 链接多个命令管道
ps = subprocess.Popen(["echo", "1"], stdout=subprocess.PIPE, shell=True)
grep = subprocess.Popen(["echo", ":"],
                        shell=True, stdin=ps.stdout, stdout=subprocess.PIPE, text=True)
ps.stdout.close()
output = grep.communicate()[0]
print(output)
# https://www.cnblogs.com/superbaby11/p/16195273.html
