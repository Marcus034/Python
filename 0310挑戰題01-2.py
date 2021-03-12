# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 18:21:09 2021

@author: USER
"""


sum = 0
a=1
b=2
n = int(input("請輸入要求和的項數:"))


for i in range(n):
    sum += b/a
    a , b = b , a+b
   

print(sum)