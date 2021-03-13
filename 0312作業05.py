# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 16:12:55 2021

@author: admin
"""
import copy

num = [10,20,30]

arr = copy.copy(num)

arr[0] = 100

print(arr)