# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 15:05:19 2021

@author: admin
"""
a = 1
x = 0
num = []

while True:
    n = a * a
    a += 1
    num.append(n)
    if num[x] - 168 in num and num[x] - 168 - 100 > 0:
        break
    x += 1
   
result = num[x]- 168 - 100
print(result)


