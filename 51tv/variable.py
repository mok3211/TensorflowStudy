#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2018-10-27
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
a = 3
#create a variable
w = tf.Variable([[0.5, 1.0]])
x = tf.Variable([[2.0],[1.0]])
y = tf.matmul(w, x)
print(w)
# variable have to be explicitly initialized
init_op = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init_op)
    print(y.eval())

# 基本操作 推荐使用float32
# 随机生成1000个点，围绕在y=0.1x+0.3 的直线周围
num_point = 1000
vectors_set = []
for i in range(num_point):
    x1 = np.random.normal(0.0, 0.55)
    y1 = x1 * 0.1 + 0.3 + np.random.normal(0.0, 0.03)
    vectors_set.append([x1, y1])

# 生成一些样本
x_data = [v[0] for v in vectors_set]
y_data = [v[1] for v in vectors_set]

plt.scatter(x_data, y_data, c='r')
plt.show()


