"""
    time 标准库
"""
import time

# 1. 获取当前时间戳
timc=time.time()
print(f"时间戳为:{timc}")

# 2. 如何进行线程休眠
time.sleep(3)

# 3. 性能计算
start_cpu_time=time.process_time()
for x in range(1,1000):
    print(f"{x} ",end='')
print()
end_cpu_time=time.process_time()
use_time=end_cpu_time-start_cpu_time
print(f"程序运行时间为:{use_time}")
# n*10**(-3)


