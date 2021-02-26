# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 15:05:04 2021

@author: admin
"""

number = int(input("請輸入次數:"))

sum = 0


for i in range(1,number+1):
    if i % 2 == 0:
        sum += i
print("總和:",sum)

        
        

        