# coding=utf-8
import pandas as pd
import numpy as np

# 统计文件中国家出现的个数，并且将国家出现次数按照降序排列


data_df = pd.read_excel(io="data_for_pandas.xlsx")
print(data_df.head(1))
print(data_df.info())
print(data_df.describe())

country = data_df["Country"]
print(country)
country_number_count = len(country.unique())
# country_number_count = len(set(country.tolist()))
print(country.unique())
print(country_number_count)
# 8
uk_number = len(country[country == 'United Kingdom'])
print(uk_number)
# 5392
# ...
