# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 19:57:59 2021

@author: USER
"""

number = list()

while len(number) <= 5:
    num = int(input("請輸入數字:"))
    number.append(num)
print("串列內容:",number)

for i in range(len(number)):
    for k in range(len(number)):
        if number[k] > number[i]:
            number[i],number[k] = number[k],number[i]


print("氣泡排序法:",number)
