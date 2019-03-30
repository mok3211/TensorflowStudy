#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from pandas import Series
fandango = pd.read_csv("../data_set/fandango_score_comparison.csv")
series_film = fandango["FILM"]
# print(series_film[0:5])
series_rt = fandango["RottenTomatoes"]
print(series_rt[0:5])

# Series (collection of valuse)
# DataFrame (collection of  Series objects)
# Panel (collection of DataFrame objects)

film_names = series_film.values
#print type(film_names)
print(film_names)
rt_scores = series_rt.values
#print rt_scores
# series_custom = Series(rt_scores, index=film_names)
# series_custom[['Minions (2015)', 'Leviathan (2014)']]

series_custom = Series(rt_scores , index=film_names)
series_custom[['Minions (2015)', 'Leviathan (2014)']]
fiveten = series_custom[5:10]
print(fiveten)
original_index = series_custom.index.tolist()
#print original_index
sorted_index = sorted(original_index)
sorted_by_index = series_custom.reindex(sorted_index)

sc2 = series_custom.sort_index()
sc3 = series_custom.sort_values()
#print(sc2[0:10])
print(sc3[0:10])

#The values in a Series object are treated as an ndarray, the core data type in NumPy
import numpy as np
# Add each value with each other
print(np.add(series_custom, series_custom))
# Apply sine function to each value
np.sin(series_custom)
# Return the highest value (will return a single value not a Series)
np.max(series_custom)

series_custom > 50
series_greater_than_50 = series_custom[series_custom > 50]

criteria_one = series_custom > 50
criteria_two = series_custom < 75
both_criteria = series_custom[criteria_one & criteria_two]
print(both_criteria)

#data alignment same index
rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])
rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])
rt_mean = (rt_critics + rt_users)/2

print(rt_mean)


#will return a new DataFrame that is indexed by the values in the specified column
#and will drop that column from the DataFrame
#without the FILM column dropped
fandango = pd.read_csv('fandango_score_comparison.csv')
print(type(fandango))
fandango_films = fandango.set_index('FILM', drop=False)
#print(fandango_films.index)

# Slice using either bracket notation or loc[]
fandango_films["Avengers: Age of Ultron (2015)":"Hot Tub Time Machine 2 (2015)"]
fandango_films.loc["Avengers: Age of Ultron (2015)":"Hot Tub Time Machine 2 (2015)"]

# Specific movie
fandango_films.loc['Kumiko, The Treasure Hunter (2015)']

# Selecting list of movies
movies = ['Kumiko, The Treasure Hunter (2015)', 'Do You Believe? (2015)', 'Ant-Man (2015)']
fandango_films.loc[movies]

#When selecting multiple rows, a DataFrame is returned,
#but when selecting an individual row, a Series object is returned instead

# returns the data types as a Series
types = fandango_films.dtypes
#print types
# filter data types to just floats, index attributes returns just column names
float_columns = types[types.values == 'float64'].index
# use bracket notation to filter columns to just float columns
float_df = fandango_films[float_columns]
#print float_df
# `x` is a Series object representing a column
deviations = float_df.apply(lambda x: np.std(x))

print(deviations)

rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_user.apply(lambda x: np.std(x), axis=1)