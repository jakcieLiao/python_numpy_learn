# coding=utf-8
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# 不同月份不同类型的电话的次数的变化情况

# 读取文件
file_path = "./911.csv"
df = pd.read_csv(file_path)

# 获取分类
temp_list = df["title"].str.split(": ")
cate_list = list([i[0] for i in temp_list])
df["cate"] = pd.DataFrame(np.array(cate_list).reshape(df.shape[0],1))

# 创建时间索引
df["timeStamp"] = pd.to_datetime(df["timeStamp"])
df.set_index("timeStamp", inplace=True)

plt.figure(figsize=(20,8),dpi=80)
# 分组
for group_name, group_data in df.groupby("cate"):
    # 对不同的分类都进行绘图
    # 按月统计
    count_by_month = group_data.resample("M").count()["title"]
    # 画图
    _x = count_by_month.index
    _y = count_by_month.values
    _x = [i.strftime("%Y-%m-%d") for i in _x]
    plt.plot(range(len(_x)), _y, label=group_name)

# 调整x轴刻度
plt.xticks(range(len(_x)), _x, rotation=45)
plt.legend(loc="best")
plt.grid(alpha=0.3)
plt.show()