"""
    math 标准库
"""
import math

# 1. 数论和表示函数
# 向上取整
res1=math.ceil(4.2)
print(f"4.2向上取整为:{res1}")
# 向下取整
res2=math.floor(4.2)
print(f"4.2向下取整为:{res2}")
# 绝对值
res3=math.fabs(-4.2)
print(f"|-4.2|={res3}")
# 阶乘 int === >>> 3 res:1*2*3
res4=math.factorial(3)
print(f"3!={res4}")
# 公约数 36 和 24 的最大公约数
gcd_number=math.gcd(36,24)
print(f"gcd(36,24)={gcd_number}")

# 2. 幂函数和对数函数 e的x次方 log
# e的多少次方
e2=math.exp(2)
print(f"e的平方为:{e2}")
# e为底的对数
xxx=math.log(2)
# 自定义对数
print(f"log以e为底,2的对数:{xxx}")
xxx=math.log(2,2)
print(f"log以2为底,2的对数:{xxx}")
# 次幂 2**3
num=math.pow(2,3)
print(f"2的3次方为:{num}")
# 平凡根
sq=math.sqrt(4)
print(f"4的平方根为:{sq}")

# 3. 三角函数 sin cos tan arcsin arccos arctan
print(math.pi) # Π
# sin
sin_number=math.sin(math.pi/2) # sin(Π/2)
print(f"sin(Π/2)={sin_number}")
# cos
cos_number=math.cos(math.pi/3) # cos(Π/3)
print(f"cos(Π/2)={cos_number}")
# arcsin
d=math.asin(1)
print(f"arcsin(1)={d}")

# 4. 角度转换
# 弧度制--->>>角度制
d=math.degrees(math.pi/3)
print(f"math.pi/3={d}")
# 角度制--->>>弧度制
r=math.radians(90)
print(f"90°={r}")

# 5. 双曲函数
# 双曲正弦函数
sinh_0=math.sinh(0)
print(f"sinh_0={sinh_0}")
# 双曲余弦函数
cosh_0=math.cosh(0)
print(f"cosh_0={cosh_0}")

# 6. 特殊函数
# 误差函数 math.erf()
check=math.erf(0.5)
print(f"0.5的误差值为:{check}")
gamma_5=math.gamma(5)
print(f"5的伽马函数返回值:{gamma_5}")
lgamma_5=math.lgamma(5)
print(f"伽马函数:5的绝对值的自然对数:{lgamma_5}")

# 7. 数学常数
print(f"Π={math.pi}")
print(f"e={math.e}")
print(f"+∞={math.inf}")
print(f"NaN={math.nan}")

# 8. 距离和精度函数
# 欧几里得距离
dist_3_4=math.dist((0,0),(3,4))
print(f"3和4的欧几里得距离为:{dist_3_4}")
# 多维欧几里得范数
hypot_3_4=math.hypot(3,4)
print(f"3和4的多维欧几里得范数为:{hypot_3_4}")
# 浮点数是否接近
judge=math.isclose(1.1,1.0999999999)
print(f"1.1和1.0999999999是否接近:{judge}")



























