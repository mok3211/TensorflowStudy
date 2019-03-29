#!/usr/bin/env python
# -*- coding: utf-8 -*-
import seaborn as sns
iris = sns.load_dataset("iris")
sns.pairplot(iris)