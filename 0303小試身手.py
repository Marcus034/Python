# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 19:40:23 2021

@author: USER
"""

import random

count = 0
ans = random.randint(1,100)
guess = 0
max = 100
min = 1


while ans != guess:
    guess = int (input("請輸入1-100之間的整數:"))
    if ans > guess:
        min = guess + 1
        print("提示:請輸入",min,"到",max,"之間的數")
    elif ans < guess:
        max = guess -1
        print("提示:請輸入",min,"到",max,"之間的數")
    count += 1
print("恭喜猜中!","共猜:",count,"次")