# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 16:10:18 2021

@author: admin
"""
num = list()
count = 3

for i in range(3):
    n = int(input("請輸入{}個數字:".format(count)))
    num.append(n)
    count -= 1

num.sort()
print(num)
