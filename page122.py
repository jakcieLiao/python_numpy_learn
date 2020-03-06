# coding=utf-8
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager
import numpy as np

# 根据文件查看评论数与喜欢的相关情况
# 使用散点图了解相关性

# 数据路径
file_path = "./18.01.11_BR_videos.csv"
# 设置字体
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\simkai.ttf")
# 读取数据
df = pd.read_csv(file_path)
# print(df.head(1))
# print(df.info())

# 获取likes和comment的数据
likes_comment_data = df[["likes", "comment_count"]]
# print(likes_comment_data)
# 获取likes和comment的数据，且喜欢数小于10000
likes_comment = likes_comment_data[likes_comment_data["likes"]<20000]
# print(likes_comment)

# 处理异常数据，如喜欢数和评论数都为0的赋值为均值
likes_comment[likes_comment==0] = np.nan
likes_comment = likes_comment.fillna(likes_comment.mean())
# print(likes_comment)

# 绘制散点图
plt.figure(figsize=(20,8), dpi=80)
plt.scatter(likes_comment["likes"], likes_comment["comment_count"])

# 调整x，y轴信息
_x_ticks = list(range(21000))[::1000]
plt.xticks(_x_ticks, _x_ticks)

# 添加信息
plt.xlabel("喜欢数", fontproperties=my_font)
plt.ylabel("评论数", fontproperties=my_font)
plt.title("观看电影评论数与喜欢数之间的关系", fontproperties=my_font)

# 网格
plt.grid(alpha=0.4)

# 显示信息
plt.show()
