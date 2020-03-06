# coding=utf-8
import pandas as pd

file_path = "./18.01.11_BR_videos.csv"

df = pd.read_csv(file_path)
print(df.head(1))
print(df.info())