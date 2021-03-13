# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 14:53:28 2021

@author: admin
"""
profit = int(input("請輸入利潤:"))

if profit <= 100000:
    bonus = profit * 0.1
elif 200000 >= profit > 100000:
    bonus = 10000 + (profit-100000) * 0.075
else:
    bonus = 10000 + 7500 + (profit - 200000) * 0.03

print("您的獎金為:{}".format(bonus))
