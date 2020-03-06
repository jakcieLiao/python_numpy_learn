# coding=utf-8
import numpy as np


# 将nan转化为每一列非nan的均值
def convert_average(t1):
    for i in range(t1.shape[1]):
        temp_col = t1[:, i]  # 当前的一列
        nan_num = np.count_nonzero(temp_col != temp_col)  # 统计当前列不为nan的个数
        if nan_num != 0:  # 不为0，说明当前列有nan
            temp_not_nan_col = temp_col[temp_col == temp_col]  # 当前列中不为nan的array
            # temp_not_nan_col.mean()，取均值
            # 将为nan的值赋值为不为nan的均值
            # temp_col[temp_col!=temp_col] = temp_not_nan_col.mean()
            temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()
    return t1

if __name__ == "__main__":
    t1 = np.arange(12).reshape(3, 4).astype("float")
    # print(t1)
    t1[1, 2:] = np.nan
    print(t1)
    # 输出
    # [[ 0.  1.  2.  3.]
    #  [ 4.  5. nan nan]
    #  [ 8.  9. 10. 11.]]
    t1 = convert_average(t1)
    print(t1)
    # 输出
    # [[0. 1. 2. 3.]
    #  [4. 5. 6. 7.]
    #  [8. 9. 10. 11.]]
