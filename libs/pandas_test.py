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
# col_names = food_info.columns.tolist()
# gram_columns = []
#
# for c in col_names:
#     if c.endswith("(g)"):
#         gram_columns.append(c)
# gram_df = food_info[gram_columns]
# print(gram_df.head(3))

# 对元素数据进行操作
# div_1000 = food_info["Iron_(mg)"] / 1000
# Adds 100 to each value in the column and returns a Series object.
# add_100 = food_info["Iron_(mg)"] + 100
# Subtracts 100 from each value in the column and returns a Series object.
# sub_100 = food_info["Iron_(mg)"] - 100
# Multiplies each value in the column by 2 and returns a Series object.
# mult_2 = food_info["Iron_(mg)"]*2
# It applies the arithmetic operator to the first value in both columns, the second value in both columns, and so on
# water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]
# water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]
# iron_grams = food_info["Iron_(mg)"] / 1000
# food_info["Iron_(g)"] = iron_grams


max_calories = food_info["Energ_Kcal"].max()
# Divide the values in "Energ_Kcal" by the largest value.
normalized_calories = food_info["Energ_Kcal"] / max_calories
normalized_protein = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
normalized_fat = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()
food_info["Normalized_Protein"] = normalized_protein
food_info["Normalized_Fat"] = normalized_fat

#print food_info["Sodium_(mg)"]
food_info.sort_values("Sodium_(mg)", inplace=True)
print(food_info["Sodium_(mg)"])
#Sorts by descending order, rather than ascending.
food_info.sort_values("Sodium_(mg)", inplace=True, ascending=False)
print(food_info["Sodium_(mg)"])