# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:46:48 2021

@author: USER
"""

number = int(input("請輸入次數:"))

for i in range(1,number+1):
    if i % 2 == 0:
        print(i)
        print("為偶數")
    else:
        print(i)
        print("為奇數")