# coding=utf-8
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager
import numpy as np

# 对比美国与中国的星巴克数量，查看中国每个省的星巴克数量
# 分组与聚合

# 数据路径
file_path = "./directory.csv"

df = pd.read_csv(file_path)
# print(df.head(1))
# print(df.info())

# 按照国家分组
grouped = df.groupby("Country")
print(grouped)

# DataFrameGroupBy
# 可以进行遍历
# for i,j in grouped:
#     print(i)
#     print("-"*100)
#     print(j,type(j))
#     print("*"*100)
# 获取美国数据
# df = df[df["Country"]=="US"]

# 可以进行聚合
country_count = grouped["Brand"].count()
# print(country_count)
# Country
# AD        1
# AE      144
# AR      108
# AT       18
# AU       22
# ...
print(country_count["US"])  # 美国的数量13608
print(country_count["CN"])  # 中国的数量2734

# # 中国每个省份的数量统计
# df_for_cn = df[df["Country"]=="CN"]
# print(df_for_cn.info())
# # 按照省份分组
# grouped_province = df_for_cn.groupby("State/Province")
# province_count = grouped_province["Brand"].count()
# print(province_count)

# 数据按照多个条件进行分组，返回Series
# grouped = df["Brand"].groupby(by=[df["Country"],df["State/Province"]]).count()
# print(grouped)
# print(type(grouped))
# 数据按照多个条件进行分组，返回DataFrame
grouped1 = df[["Brand"]].groupby(by=[df["Country"],df["State/Province"]]).count()
print(grouped1)
print(type(grouped1))

# 索引的方法和属性，page136
print(grouped1.index,type(grouped1.index))