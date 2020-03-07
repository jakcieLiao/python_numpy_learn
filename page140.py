# coding=utf-8
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager
import numpy as np

# 画出店铺总数排名前10的国家
# 呈现中国每个城市的店铺数量

# 数据路径
file_path = "./directory.csv"
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\simkai.ttf")

df = pd.read_csv(file_path)
print(df.head(1))
print(df.info())

# 获取每个国家的店铺数量
# grouped_country = df.groupby("Country")
# # print(grouped_country,type(grouped_country))
# # # 进行遍历
# # for i,j in grouped_country:
# #     print(i)
# #     print("-"*100)
# #     print(j,type(j))
# #     print("*"*100)
#
# # 计算每个国家的数量
# grouped_count = grouped_country["Brand"].count()
# print(grouped_count)
# grouped_count = grouped_count.sort_values(ascending=False)
# print(grouped_count)
# grouped_count = grouped_count[:10]
# print(grouped_count)

# # 准备店铺数量排名前10的数据
# data = df.groupby(by="Country").count()["Brand"].sort_values(ascending=False)[:10]
# print(data, type(data))
#
# # 绘制，使用条形图
# plt.figure(figsize=(20,8),dpi=80)
# plt.bar(data.index, data.values)
# plt.show()

# ****************************************************************************************************
# 准备中国的各个城市的店铺数量
data1 = df[df["Country"] == "CN"].groupby("City")["Brand"].count().sort_values(ascending=False)[:20]
print(data1.index)
print("*"*100)
print(data1.values)
# 绘制，使用条形图
plt.figure(figsize=(20,8),dpi=80)
# plt.bar(range(len(data1.index)), data1.values)
# _x = len(data1.index)
# plt.xticks(range(_x), data1.index, fontproperties=my_font)
plt.barh(range(len(data1.index)), data1.values, height=0.5, color="orange")
_x = len(data1.index)
plt.yticks(range(_x), data1.index, fontproperties=my_font)
plt.grid(alpha=0.4)
plt.show()