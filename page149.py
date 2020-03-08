# coding=utf-8
import pandas as pd
from matplotlib import pyplot as plt

# 北京PM2.5随时间2010年至2015的变化情况，中国与美国做对比

# 读取数据
file_path = "./BeijingPM20100101_20151231.csv"
df = pd.read_csv(file_path)

# 重组时间序列
datetime = pd.PeriodIndex(year=df["year"],month=df["month"],day=df["day"],freq="D")
df["date"] = datetime

# 设置时间戳为索引
df.set_index("date", inplace=True)

# 以PM_US Post为准绘制图表
data = df.resample("7D").mean()["PM_US Post"]
data_china = df.resample("7D").mean()["PM_Dongsi"]

# 绘制
plt.figure(figsize=(20,8),dpi=80)

_x = data.index
_y = data.values
_x_china = data_china.index
_y_china = data_china.values
plt.plot(range(len(_x)),_y,label="PM_US")
plt.plot(range(len(_x_china)),_y_china,label="PM_CN")

# 调整x轴刻度
plt.xticks(list(range(len(_x)))[::10], _x[::10],rotation=45)

# 添加辅助描述
plt.legend(loc="best")
plt.grid(alpha=0.3)

# 展示
plt.show()
