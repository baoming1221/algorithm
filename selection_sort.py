# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 18:48
# @Author  : Alessia
# @Email   : baoming1221@126.com
# @File    : selection_sort.py
# @Software: PyCharm

#选择排序
'''
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置

再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。

重复第二步，直到所有元素均排序完毕。
'''
#nums = [4,2,3,6,5]
# nums1 = [6,3,8,1,5]
#
# def slt_sort(a):
#     for i in range(len(a)):
#         min = i
#         j = i + 1
#         for j in range(len(a)):
#             if a[j] <= a[min]:
#                 min = j
#             else:
#                 pass
#         if i != min:
#             tmp = a[min]
#             a[min] = a[i]
#             a[i] = tmp
#     return a
# print(slt_sort(nums))

a = [6,9,3,5,0,1,4,2,7]
def slc_sort(t):
    for i in range(len(a)-1):
        min = i
        for j in range(i+1,len(a)):
            if a[min] >= a[j]:
                min = j
        k = a[min]
        a[min] = a[i]
        a[i] = k
    return a

print(slc_sort(a))
