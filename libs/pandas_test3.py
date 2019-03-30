#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

ttnic = pd.read_csv("../data_set/titanic_train.csv")
# print(ttnic.head())
age = ttnic["Age"]
# print(age.head(5))
# age_is_null = pd.isnull(age)
# print(age_is_null)
#
# age_null_true = age[age_is_null]
# print(age_null_true)

# 在统计age时先过滤age为空
# good_age = ttnic["Age"][age_is_null == False]
# print(good_age)
# corrent_mean_age = sum(good_age)/len(good_age)
# print(corrent_mean_age)

# 调用mean 方法 pandas 会自动过滤掉null 值
# corrent_mean_age_2 = ttnic["Age"].mean()
# print(corrent_mean_age_2)

# Class
# passenger_classes = [1, 2, 3]
# fares_by_class = {}
# for this_class in passenger_classes:
#     pclass_rows = ttnic[ttnic["Pclass"] == this_class]
#     print(pclass_rows.head(3))
#     pclass_fares = pclass_rows["Fare"]
#     fare_for_class = pclass_fares.mean()
#     print(fare_for_class)
#     fares_by_class[this_class] = fare_for_class
# print(fares_by_class)

# 调用pivot_table 进行数据计算
# pivot_table index 参数tells the method which column to group by
# values is the column that we want to apply the calculation to
# aggfunc specifies the caculation we want to perform
# passenger_survival = ttnic.pivot_table(index="Pclass", values="Survived", aggfunc=np.mean)
# print(passenger_survival)

# specigying axis=1 or axis= "columns" will drop any columns that have null values
# drop_na_columns = ttnic.dropna(axis=1)
# print(drop_na_columns)
# new_titnic_suvival = ttnic.dropna(axis=0, subset=["Age", "Sex"])
# print(new_titnic_suvival)
# row_index_83 = ttnic.loc[83, "Age"]
# row_index_1000_pclass = ttnic.loc[766, "Pclass"]
# print(row_index_83)
# print(row_index_1000_pclass

# new_titanic_survival = ttnic.sort_values("Age", ascending=False)
# print(new_titanic_survival[0:10])
# ttnic_reindexed = new_titanic_survival.reset_index(drop=True)
# print(ttnic_reindexed[0:10])

# this function returns the hundredth item from a series


# def hundredth_row(column):
#     # Extract the hundredth item
#     hundredth_item = column.iloc[99]
#     return hundredth_item
#
#
# # return the hundredth item from each column
# hundredth_row = ttnic.apply(hundredth_row)
# print(hundredth_row)

def which_class(row):
    pclass = row["Pclass"]
    if pd.isnull(pclass):
        return "Unknown"
    elif pclass == 1:
        return "First Class"
    elif pclass == 2:
        return "Second Class"
    elif pclass == 3:
        return "Third Class"


classes = ttnic.apply(which_class, axis=1)
print(classes)