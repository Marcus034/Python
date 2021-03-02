# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 22:42:41 2021

@author: admin
"""
num = int(input("請輸入數值:"))
sum = 0

for num in range(1,num+1):
    sum += num
print("1~您輸入的數值加總為:",sum)
    