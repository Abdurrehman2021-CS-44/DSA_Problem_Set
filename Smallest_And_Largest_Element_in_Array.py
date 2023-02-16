# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 23:08:34 2022

@author: USER
"""

def maximum(arr):
    largest = -1
    largest_idx = 0
    for i in range(0, len(arr), 1):
        if (largest < arr[i]):
            largest = arr[i]
            largest_idx = i
    return largest_idx

def minimum(arr):
    smallest = 100000
    smallest_idx = 0
    for i in range(0, len(arr), 1):
        if (smallest > arr[i]):
            smallest = arr[i]
            smallest_idx = i
    return smallest_idx
    
arr = [22,14,8,17,35,8]
largest_idx = maximum(arr)
smallest_idx = minimum(arr)

print("Maximum Number:" + str(arr[largest_idx]))
print("Minimum Number:" + str(arr[smallest_idx]))