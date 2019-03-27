# -*- coding: utf-8 -*-
# !/usr/bin/python
import numpy
world_alchohol = numpy.genfromtxt("../data_set/world_alcohol.txt", delimiter=",")


# array()
vector = numpy.array([5, 10, 15, 20])
matrix = numpy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

print(vector.shape)
print(matrix.shape)

numbers = numpy.array([1, 2, 3, 4])
print(numbers.dtype)

uruguay_other_1986 = world_alchohol[1, 4]
third_country = world_alchohol[2, 2]
print(uruguay_other_1986)
print(third_country)
