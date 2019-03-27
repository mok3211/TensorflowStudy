# -*- coding: utf-8 -*-
# !/usr/bin/python
import numpy
world_alchohol = numpy.genfromtxt("../data_set/world_alcohol.txt", delimiter=",")


# array()
# vector = numpy.array([5, 10, 15, 20])
# matrix = numpy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
#
# print(vector.shape)
# print(matrix.shape)
#
# numbers = numpy.array([1, 2, 3, 4])
# print(numbers.dtype)
#
# uruguay_other_1986 = world_alchohol[1, 4]
# third_country = world_alchohol[2, 2]
# print(uruguay_other_1986)
# print(third_country)

# 判断某些项的值 以dtype = bool 返回
# vector = numpy.array([5, 10, 15, 20])
# print(vector == 10)

# matrix = numpy.array([
#                 [5, 10, 15],
#                 [20, 25, 30],
#                 [35, 40, 45]
#              ])
# second_column_25 = (matrix[:,1] == 25)
# print(second_column_25)
# print(matrix[second_column_25, :])

# vector = numpy.array([5, 10, 15, 20])
# res = (vector == 10) & (vector == 5)
# res = (vector == 10) | (vector == 5)
# print(res)

# vector = numpy.array([5, 10, 15, 20])
# # res = (vector == 10) | (vector == 5)
# # vector[res] = 100
# # print(vector)
# matrix = numpy.array([
#             [5, 10, 15],
#             [20, 25, 30],
#             [35, 40, 45]
#          ])
#
# res = matrix[:, 1]
# print(res)
# print(res)
# matrix[res, 1] = 10
# print(matrix)

# vector = numpy.array(["1", "2", "3"])
# vector = vector.astype(float)
# print(vector)
# vector = numpy.array([10, 20, 30, 40])
# print(vector.sum())
matrix = numpy.array([
                [5, 10, 15],
                [20, 25, 30],
                [35, 40, 45]
             ])
res = matrix.sum(axis=1)
print(res)