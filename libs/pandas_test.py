#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd

# pands 读取数据集
food_info = pd.read_csv("../data_set/food_info.csv")
# print(food_info)
# print(food_info.dtypes)

# 获取片段信息
# first_rows = food_info.head()
# food_info.head(3)
# food_info.columns
# food_info.shape

# food_info.loc[0]
# food_info.loc[6]
# object - For string values
# int - For integer values
# float - For float values
# datetime - For time values
# bool - For Boolean values
# print(food_info.dtypes)

# 返回 DataFrame 包含3，4，5，6 indexs
# print(food_info.loc[3:6])

# 返回任意indexs 行
# print(food_info.loc[[2, 5, 10]])

# 返回指定的行名数据

#ndb_col = food_info["NDB_No"]
#print ndb_col
# Alternatively, you can access a column by passing in a string variable.
#col_name = "NDB_No"
#ndb_col = food_info[col_name]

#columns = ["Zinc_(mg)", "Copper_(mg)"]
#zinc_copper = food_info[columns]
#print zinc_copper
# Skipping the assignment.
#zinc_copper = food_info[["Zinc_(mg)", "Copper_(mg)"]]
# print(food_info.columns.tolist())
col_names = food_info.columns.tolist()
gram_columns = []

for c in col_names:
    if c.endswith("(g)"):
        gram_columns.append(c)
gram_df = food_info[gram_columns]
print(gram_df.head(3))