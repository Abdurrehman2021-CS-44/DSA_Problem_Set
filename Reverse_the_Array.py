# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 12:59:47 2022

@author: USER
"""

arr = [1,2,3,4,5,6,7,8,9]

def reverse_array(arr):
    A = []
    for i in range(len(arr)-1,-1,-1):
        A.append(arr[i])
    return A

A = reverse_array(arr)
print(arr)
print(A)