"""
    datetime 模块
"""
import datetime

# 1. 获取当前时间和日期
now_time=datetime.datetime.now()
print(f"当前时间为:{now_time}")

# 2. 创建特定日期和时间对象
mc=datetime.date(2025,1,1)
print(f"这是我创建的时间:{mc}")

# 3. 解析字符串时间
# 2025=2=1 2025年2月1日
strs="2025=2+1"
format_time=datetime.datetime.strptime(strs,"%Y=%m+%d")
print(f"解析之后的时间为:{format_time}")

# 4. 时间的加减法
# datetime 一天的时间单位是datetime.timedelta(days=1)
now=datetime.datetime.now()
now_next=now+datetime.timedelta(days=1,seconds=60)
print(f"今天日期为:{now}")
print(f"明天日期为:{now_next}")

# 5. 提取年月日 时分秒
now=datetime.datetime.now()
print(f"年:{now.year};月:{now.month};日:{now.day}")

# 6. 替换日期时间部分
now=datetime.datetime.now()
print(f"当前错误时间:{now}")
# 2035年1月1日
new_time=now.replace(year=2035,month=1,day=1,hour=23)
print(f"更改之后的时间为:{new_time}")




