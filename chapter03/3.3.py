#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
"""
Tensorflow 运行模型 - 会话 session
会话拥有并管理TensorFlow 程序运行时的所有资源 所有计算完成之后需要关闭session 回收资源
一般使用会话的模式有两种 1。需要明确调用会话生成函数和关闭会话函数 2。
"""

# 模式一
a = tf.constant([1.0, 2.0], name='a')
b = tf.constant([2.0, 3.0], name='b')
result = tf.add(a, b, name='add')
# 创建一个会话
sess = tf.Session()
# 使用会话得到运算结果， 调用sess.run(result)
print(sess.run(result))
# 关闭会话使得本次运行中使用的资源释放
sess.close() # 使用模式一必须关闭会话 否则会导致资源泄漏

# 改进版 使用python 上下文管理器来管理这个会话
with tf.Session() as sess:
    # 使用创建好的会话来计算结果
    res = sess.run(result) # 上下文退出时会话资源释放也就自动完成
    result.eval(session= sess) # 与前者作用一样

# 交互模式下使用session
# sess = tf.InteractiveSession()
# print(sess.eval())
# sess.close()




