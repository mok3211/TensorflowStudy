#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tensorflow as tf
# tf.constant 是一个计算，这个计算的结果为一个张量，保存在变量a中
a = tf.constant([1.0, 2.0], name='a')
b = tf.constant([2.0, 3.0], name='b')
result = tf.add(a, b, name='add')
print(result)  #运行结果是一个张量的结构 Tensor("add:0", shape=(2,), dtype=float32) 依次为name shape(维度)， type(类型)

# Tensorflow 支持14中不同的类型，实数tf.float32, tf.float64 整数（tf.int8, tf.int16, tf.int32, tf.int64,
# tf.unit8） Bool型tf.bool 和复数 tf.complex64 tf.complex128

#tenserflow 数据模型使用 分为两类

# 第一类 对计算中间计算结果引用

# 第二类 当计算图构造完成后


