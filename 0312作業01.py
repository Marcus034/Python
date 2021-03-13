# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 14:37:38 2021

@author: admin
"""

num = [1,2,3,4]

result = list()

for i in num:
    for j in num:
        for k in num:
            if len(set((i,j,k))) == 3:
                result.append((i,j,k))
print("排列組合有{}種,組合有下列{}".format(len(result),result))
