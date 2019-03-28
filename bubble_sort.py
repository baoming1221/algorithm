# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 17:11
# @Author  : Alessia
# @Email   : baoming1221@126.com
# @File    : bubble_sort.py
# @Software: PyCharm

nums = [5,4,2,3,8]

def bubble(a):
    i = 1
    j = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if a[j] <= a[i]:
                pass
            else:
                b = a[i]
                a[i] = a[j]
                a[j] = b
    return a

print(bubble(nums))


