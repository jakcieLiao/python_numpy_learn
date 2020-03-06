# coding=utf-8
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 统计文件中Description 中每个单词出现的次数，并画出条形图

data_df = pd.read_excel(io="data_for_pandas.xlsx")
# print(data_df.head(1))
# print(data_df.info())
# print(data_df.describe())

# 提取前20行的Description
phrase_list = data_df[:5]["Description"]
print(phrase_list)

#  统计单词列表
temp_list = phrase_list.str.split(" ").tolist()
print(temp_list)
# [['WHITE', 'HANGING', 'HEART', 'T-LIGHT', 'HOLDER'], ['WHITE', 'METAL','LANTERN'], ..]]
# 将大的列表转换为一串列表
danci_list = list(set([i for j in temp_list for i in j]))   # set 去重
print(danci_list)
# ['', '6', 'HEART.', 'HEART', 'FLAG', 'WATER', 'CHARLOTTE', ...]
# 构造全为0的数组
zeros_df = pd.DataFrame(np.zeros((len(phrase_list), len(danci_list))), columns=danci_list)
# print(zeros_df)

# 给每个短语出现单词的位置赋值1
for i in range(phrase_list.shape[0]):
    # zeros_df.loc[0, ['WHITE', 'HANGING', 'HEART', 'T-LIGHT', 'HOLDER']] = 1
    zeros_df.loc[i, temp_list[i]] = 1

# print(zeros_df.head(3))

# 统计每个单词出现的次数
danci_count = zeros_df.sum(axis=0)
print(danci_count)

# 排序
danci_count = danci_count.sort_values()
# print(type(danci_count))

# 绘制
_x = danci_count.index
_y = danci_count.values
plt.figure(figsize=(20,8), dpi=80)
plt.bar(range(len(_x)), _y, width=0.7)
plt.xticks(range(len(_x)), _x)
plt.show()
