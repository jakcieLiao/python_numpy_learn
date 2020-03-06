# coding=utf-8
import numpy as np
from matplotlib import pyplot as plt

# 希望了解英国的youtube中视频的评论数和喜欢数的关系，应该如何绘制改图
# 第一列为点赞，第二列为喜欢，第三列为不喜欢，第四列为评论，总共一千条数据
t_ua = np.arange(4000).reshape(1000, 4)

# 选择喜欢数小于3000的,并且可以使得喜欢数与评论数对应
t_ua = t_ua[t_ua[:, 1]<3000]

t_ua_likes = t_ua[:, 1]
t_ua_comments = t_ua[:, 3]
x = t_ua_likes
y = t_ua_comments

# 绘制散点图
plt.figure(figsize=(20,8), dpi=80)
plt.scatter(x,y)

# # 调整x刻度
# plt.xticks(list(range(3000))[::100])

# 网格
plt.grid(alpha=0.4)

plt.show()
