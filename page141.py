# coding=utf-8
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager
import numpy as np

# 不同年份书的数量
# 不同年份书的平均评分情况

# 数据路径
file_path = "./books.csv"
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\simkai.ttf")
df = pd.read_csv(file_path)
# print(df["original_publication_year"].describe())
# count    9979.000000
# mean     1981.987674
# std       152.576665
# min     -1750.000000
# 25%      1990.000000
# 50%      2004.000000
# 75%      2011.000000
# max      2017.000000

# 不同年份书的数量
# 去除nan的数据
data1 = df[pd.notnull(df["original_publication_year"])]
# year_count = data1.groupby("original_publication_year")["authors"].count().sort_values(ascending=True)
# print(year_count)


# ********************************************************************************************
# 不同年份书的平均评分情况
average_rating = data1["average_rating"].groupby(by=data1["original_publication_year"]).mean()
# print(average_rating)

# 使用折线图显示平均评分的变化情况
_x = average_rating.index
_y = average_rating.values
# print(_x, _y)

# 绘制
plt.figure(figsize=(20,8),dpi=80)
plt.plot(range(len(_x)), _y)

# 调整x轴
plt.xticks(list(range(len(_x)))[::10], _x.astype(int)[::10])

# 网格
plt.grid(alpha=0.4)

plt.show()

