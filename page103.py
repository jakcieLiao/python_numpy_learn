# coding=utf-8
import pandas as pd

print(pd.Series([1,5,2,4]))
print(pd.Series([1,5,4,4],index=list("abcd")))  # 通过列表创建
temp_dict = {"name":"xiaojiang","age":18,"tel":10068}   # 通过字典创建
t3 = pd.Series(temp_dict)
print(t3)
# name    xiaojiang
# age            18
# tel         10068
for i in t3.index:
    print(i)
# name
# age
# tel

for i in t3.values:
    print(i)
# xiaojiang
# 18
# 10068

# t3[["age"]]
# age    18
# dtype: object
# t3[1]
# 18
# t3[[1]]
# age    18
# dtype: object

# where方法
t4 = pd.Series(range(5))
print(t4.where(t4>2))
# 0    NaN
# 1    NaN
# 2    NaN
# 3    3.0
# 4    4.0
# dtype: float64