# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 16:10
# @Author  : Alessia
# @Email   : baoming1221@126.com
# @File    : move_zeros.py
# @Software: PyCharm


'''
给定一个数组nums，写一个函数，将数组中所有的0挪到数组的末尾，⽽维持其他所有非0元素的相对位置。
举例: nums = [0, 1, 0, 3, 12]，函数运⾏后结果为[1, 3, 12, 0, 0]

参考：https://mp.weixin.qq.com/s/ikxTnt9kpCtxHmosCjxcuw
'''


nums = [0, 1, 0, 3, 12]

# #method 1
# def move_zero(a):
#     b = []
#     c = 0
#     for i in range(len(a)):
#         if a[i]==0:
#             c += 1
#         else:
#             b.append(a[i])
#
#     while c>0:
#         b.append(0)
#         c -= 1
#     return b

# #method 2
# def move_zero(a):
#     k = 0
#     for i in range(len(a)):
#         if a[i] != 0:
#             a[k] = a[i]
#             k += 1
#
#     while k < len(a):
#         a[k] = 0
#         k += 1
#     return a

#method 3


print(move_zero(nums))

