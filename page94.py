# coding=utf-8
import numpy as np

t_ua = np.arange(4000).reshape(1000, 4)
t_uk = np.arange(4000,8000).reshape(1000, 4)

# 添加国家信息
zeros_data = np.zeros((t_ua.shape[0],1)).astype(int)
ones_data = np.ones((t_uk.shape[0],1)).astype(int)

# 分别添加一列全为0，1的数组
t_ua = np.hstack((t_ua,zeros_data))
t_uk = np.hstack((t_uk,ones_data))

# 拼接两组数据
final_data = np.vstack((t_ua,t_uk))
print(final_data)

# 创建一个全为0的数组
print(np.zeros((3,4)))
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

# 创建一个全为1的数组
print(np.ones((3,4)))
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

# 创建对角线为一的方阵
print(np.eye(5))
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]

# 最值的位置
# t = np.eye(4)
print(np.argmax(t_uk,axis=0))
print(np.argmin(t_uk,axis=0))
# [999 999 999 999   0]
# [0 0 0 0 0]
# print(np.argmin(t_uk,axis=1))

# numpy生成随机数
np.random.seed(1)   # 可以使得每次运行的随机数生成是一样的
print(np.random.rand(3,4))  # 生成多维度的均匀分布，范围为0-1
print(np.random.randn(3,4)) # # 生成多维度的正态分布，范围为-1-1
print(np.random.randint(10,20,(3, 4)))  # 整数
print(np.random.uniform(10,20,(3, 4)))  # 小数
# [[4.17022005e-01 7.20324493e-01 1.14374817e-04 3.02332573e-01]
#  [1.46755891e-01 9.23385948e-02 1.86260211e-01 3.45560727e-01]
#  [3.96767474e-01 5.38816734e-01 4.19194514e-01 6.85219500e-01]]
# [[ 0.3190391  -0.24937038  1.46210794 -2.06014071]
#  [-0.3224172  -0.38405435  1.13376944 -1.09989127]
#  [-0.17242821 -0.87785842  0.04221375  0.58281521]]
# [[14 18 11 14]
#  [10 13 19 12]
#  [10 14 19 12]]

# ******************************************
# copy 和 view
a = np.arange(6).reshape(2,3)
print(a)
b = a
print(b)
# 赋值会改变
b[1,1] = 10
print(a[1,1])
# 10
print("*"*50)
# 切片会改变
c = a[:,2]
print(c)
c[0] = 20
print(a)
# [[ 0  1 20]
#  [ 3 10  5]]
# 使用reshape不会改变
b = b.reshape(3,2)
print(b)
print(a)
# [[ 0  1]
#  [20  3]
#  [10  5]]
# [[ 0  1 20]
#  [ 3 10  5]]

