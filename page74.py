# coding=utf-8
import numpy as np

t1 = np.arange(50).reshape(5, 10)
print(t1)
print("*"*50)

# 转置
# t2 = t1.T
# t2 = t1.transpose()
# t2 = t1.swapaxes(1,0)
# print(t2)

# **************************************************
# page78切片
# print("*" * 50)
# 取行
# print(t1[2])
# print(t1[2, :])
# 取连续的多行
# print(t1[2:])
# print(t1[2:, :])
# 取不连续的多行
# print(t1[[0, 2, 4]])
# print(t1[[0, 2, 4], :])

# 取列
# print(t1[:,1])
# # 取连续列
# print(t1[:,2:])
# # 取不连续的列
# print(t1[:, [1, 5, 4]])
#
# # 取行和列，如第五行第四列
# print(t1[4,3])
# # 取连续的行和列，如第2行到第四行，同时第三列到第五列
# print(t1[1:4, 2:5])
# # 取不连续的行和列(1,2)(5,6)(3,9)
# print(t1[[1,4,3], [2,6,9]])

# **************************************************
# 赋值
# print(t1)
# print(t1>10)
# # 大于10的赋值为20，小于或等于10的赋值为5
# print(np.where(t1>10,20,5))
# 大于20的赋值为nan
t1 = t1.astype("float") # 首先需要先将integer类型转化为float，然后再赋值为nan
t1[t1>20] = np.nan
print(t1)
# # print(np.nan == np.nan)   # false
# clip裁剪，大于18.1的赋值为18.1，小于10.1的赋值为10.1
print(t1.clip(18.1, 10.1))
print(t1.clip(18.1))
# # 输出
# [[10.1 10.1 10.1 10.1 10.1 10.1 10.1 10.1 10.1 10.1]
#  [10.1 11.  12.  13.  14.  15.  16.  17.  18.  18.1]
#  [18.1  nan  nan  nan  nan  nan  nan  nan  nan  nan]
#  [ nan  nan  nan  nan  nan  nan  nan  nan  nan  nan]
#  [ nan  nan  nan  nan  nan  nan  nan  nan  nan  nan]]

# *******************************************
# 将第一列赋值为0
t1[:,0] = 0
print(t1)
# 输出
# [[ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9.]
#  [ 0. 11. 12. 13. 14. 15. 16. 17. 18. 19.]
#  [ 0. nan nan nan nan nan nan nan nan nan]
#  [ 0. nan nan nan nan nan nan nan nan nan]
#  [ 0. nan nan nan nan nan nan nan nan nan]]
# 统计不为0的数据的个数
print(np.count_nonzero(t1))
# 统计nan的个数
print(np.count_nonzero(np.isnan(t1)))
print(np.count_nonzero(t1[t1!=t1]))
# 计算和
t2 = np.arange(20).reshape(4,5)
print(t2)
print(np.sum(t2))
# 计算某一列的和
t2 = t2.astype("float")
t2[3,2] = np.nan
print(t2)
print(np.sum(t2))
# 计算列的和
print(np.sum(t2,axis=0))
print(t2.sum(axis=0))
# 计算行的和
print(np.sum(t2,axis=1))
print(t2.sum(axis=1))
# 计算列的均值
print(t2.mean(axis=0))
print(np.median(t2,axis=0))
# 极值
print(t2.min(axis=0))
print(t2.max(axis=0))
# 极值之差
print(np.ptp(t2, axis=0))
# 标准差,保留两位小数
print(np.round(t2.std(axis=0),2))