"""
    random package
"""
import random

# 1. 整数随机数生成
# 生成从0-n之间随机数
res=random.randrange(100)
print(f"0-100之间随机数为:{res}")
# 生成指定区间内随机数
res=random.randint(999,9999)
print(f"指定区间内随机数为:{res}")

# 2. 序列操作
# 等权重选出一个元素
names=["jom","kom","lom"]
res=random.choice(names)
print(f"从{names}中随机选出一个:{res}")
# 指定权重
res=random.choices(names,weights=[1,1,1],k=2)
print(f"权重为[0,1,0],选择结果为:{res}")

# 3. 浮点数随机分布
# 均匀分布
res=random.uniform(2.5,5.5)
print(f"2.5-5.5之间的均匀分布结果为:{res}")
# 三角分布 (low,high,mode)
res=random.triangular(0,10,5)
print(f"三角分布结果为:{res}")
# 指数分布
res=random.expovariate(1.0/5)
print(f"指数分布结果为:{res}")
# Beta 分布
res=random.betavariate(0.5,0.5)
print(f"0.5&0.5的Bate分布结果为:{res}")
# Gama分布 (alpha,beta)
res=random.gammavariate(1.0,2.0)
print(f"Gama分布计算结果为:{res}")
# 高斯分布 正态分布
res=random.gauss(0,1)
print(f"0-1之间的高斯正态分布结果为:{res}")
# 对数正态分布
res=random.lognormvariate(0,0.5)
print(f"0-0.5之间的对数正态分布:{res}")
# 循环正态分布
res=random.vonmisesvariate(0,4)
print(f"0-4之间的循环正态分布:{res}")
# WeiBull 分布 (alpha,beta)
res=random.weibullvariate(1.0,1.0)
print(f"1.0&1.0的WeiBull分布结果为:{res}")

# 4. 系统随机源(安全相关)
# 创建SystemRandom系统随机源对象
res=random.SystemRandom()
print(f"生成安全的浮点数:{res.random()}")
print(f"生成n个随机字节:{res.randbytes(16)}")




