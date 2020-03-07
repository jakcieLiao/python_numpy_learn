# coding=utf-8
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager
import numpy as np

# 不同类型的紧急情况的次数

file_path = "./911.csv"
df = pd.read_csv(file_path)

# 获取分类
# 方法一：在dataFrame数据末尾添加一列数据，然后使用groupby聚合统计
temp_list = df["title"].str.split(": ").tolist()
cate_list = list([i[0] for i in temp_list])
df["cate"] = pd.DataFrame(np.array(cate_list).reshape(df.shape[0],1))
sum_cate = df.groupby("cate").count()["title"]
print(sum_cate)
# EMS        208676
# Fire        63775
# Traffic    151458

# # 方法二：构造全为0的数组，然后赋值，再进行统计
# # print(df["title"].str.split(": "))
# temp_list = df["title"].str.split(": ").tolist()
# cate_list = list(set(i[0] for i in temp_list))
# # 构造全为0的数组
# zeros_df = pd.DataFrame(np.zeros((df.shape[0],len(cate_list))), columns=cate_list)
# # 赋值
# # 只用遍历3次数据，按列遍历
# for cate in cate_list:
#     zeros_df[cate][df["title"].str.contains(cate)] = 1
# sum_ret = zeros_df.sum(axis=0)
# print(sum_ret)
# # 遍历250000条数据，速度很慢
# # for i in range(df.shape[0]):
# #     zeros_df.loc[i, temp_list[i][0]] = 1
# # print(zeros_df)
