# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:35:27 2021

@author: USER
"""

import random

num = list()

while len(num) <= 5:
    n = random.randint(1,49)
    if num.count(n) == 0:
        num.append(n)
    
print("這是您的電腦選號:",num)