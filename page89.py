# coding=utf-8
import numpy as np
from matplotlib import pyplot as plt

# 英国和美国各自youtube1000的数据结合之前的matplotlib绘制出各自的评论数量的直方图
# 第一列为点赞，第二列为喜欢，第三列为不喜欢，第四列为评论，总共一千条数据
t_ua = np.arange(4000).reshape(1000, 4)
t_ua_comments = t_ua[:,3]

# 获取评论的数据
print(t_ua_comments.min(),t_ua_comments.max())

# 选择比3500小的数据
t_ua_comments = t_ua_comments[t_ua_comments<3000]

# 组数
# d = 200 # 组距
d = 100
x_bins = (t_ua_comments.max()-t_ua_comments.min())//d

# 绘制
plt.figure(figsize=(20,8), dpi=80)
plt.hist(t_ua_comments, x_bins)

# 调整x刻度
plt.xticks(list(range(3000))[::100])

# 网格
plt.grid(alpha=0.4)

plt.show()
