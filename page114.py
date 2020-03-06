# coding=utf-8
import pandas as pd
import numpy as np

data_df = pd.read_excel(io="data_for_pandas.xlsx")
df = pd.DataFrame(data_df)

# print(df)

# 显示头五行
# print(df.head(1))
# print(df.tail())

# 展示df的概览
# print(df.info())
# print(df.describe())

# 切割
# print(df["Country"].str.split(" ").tolist())

# 统计某一个数据出现的次数
# dataFrame中排序的方法
df = df.sort_values(by="CustomerID",ascending=False)
# print(df.head())

# pandas取行或者列的注意点
# - 方括号写数组，表示取行，对行进行操作
# - 写字符串，表示取列索引，对列进行操作，取列之后为Series类型
# print(df[:20])
# print(df[:20]["CustomerID"])
# print(type(df["CustomerID"]))   # <class 'pandas.core.series.Series'>

# pandas的其他取行列方法
# df.loc通过标签索引行数据
# df.iloc通过位置获取行数据
df1 = pd.DataFrame(np.arange(24).reshape(4,6),index=list("ABCD"),columns=list("QRWXYZ"))
print(df1)
print(df1.loc[["A","C"],["X","Z"]])
#     X   Z
# A   3   5
# C  15  17
print(df1.loc["A",["X","Z"]])
# X    3
# Z    5
# Name: A, dtype: int32
print(df1.loc[["A","C"],"X"])
# A     3
# C    15
# Name: X, dtype: int32
print(df1.loc["A",:])
# 注意使用标签索引的时候可以选中C行
print(df1.loc["A":"C","R":"X"])
#     R   W   X
# A   1   2   3
# B   7   8   9
# C  13  14  15
print(df1.iloc[1:3,2:4])
#     W   X
# B   8   9
# C  14  15

# pandas 中对于nan和0的处理
# nan
df2 = pd.DataFrame(np.arange(12).reshape(3,4))
df2[(df2>10)|(df2<2)] = np.nan
print(df2)
# 判断是否为nan
print(pd.isnull(df2))
print(pd.notna(df2))
# 删除nan所在的行列，
# df2.dropna(axis=0,how="any",inplace=True)
# print(df2)
# 1  4.0  5.0  6  7.0
# # 填充nan数据为当前列的平均值
# df2.fillna(df2.mean(),inplace=True)
# print(df2)
# 使用df.iloc[]定位到我们需要修改的行，然后进行修改
# df2.iloc[:, [0, 1]] = df2.iloc[:,[0,1]].fillna(df2.iloc[:,[0,1]].mean())
print(df2)
# 0,nan在pandas中不会被统计计算均值，0会
# df2[df2==0] = np.nan