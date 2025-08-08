"""
    数学和数值计算
    statistics
"""

import statistics as st

# 1. 集中趋势度量
nums=[1,2,3,4]
# 算数平均数 mean() 
mean_number=st.mean(nums)
print(f"算数平均数为:{mean_number}")
# 快速浮点平均数 fmean()
fnums=[1.1,2.2,3.3]
print(f"快速浮点平均数:{st.fmean(fnums)}")
# 中位数
print(f"中位数:{st.median(nums)}")
# 众数 出现次数最多的元素
some=[1,2,3,1,1]
print(f"{some}中的众数为:{st.mode(some)}")
# 调和平均数
print(f"{nums}调和平均数:{st.harmonic_mean(nums)}")
# 几何平均数
print(f"{nums}几何平均数:{st.geometric_mean(nums)}")

# 2. 离散程度度量
# 样本
nums=[1,2,3,4]
# 样本方差
print(f"{nums}样本方差为:{st.variance(nums)}")
# 总体方差
print(f"总体方差:{st.pvariance(nums)}")
# 样本标准差
print(f"样本标准差:{st.stdev(nums)}")
# 总体标准差
print(f"总体标准差:{st.pstdev(nums)}")
# 分位数 四分位相等 
print(f"分位数 n=4:{st.quantiles(nums,n=4)}")

# 3. 相关性度量 python--version>=3.10
nums1=[1,2,3]
nums2=[4,5,6]
# 皮尔逊相关系数
p=st.correlation(nums1,nums2)
print(f"{nums1}与{nums2}的皮尔逊相关系数为:{p}")
# 样本协方差
c=st.covariance(nums1,nums2)
print(f"样本协方差:{c}")
# 线性回归斜率/截距
s,i=st.linear_regression(nums1,nums2)
print(f"线性回归:斜率和截距分别为:{s}&{i}")



















