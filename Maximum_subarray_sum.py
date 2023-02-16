# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 13:14:19 2022

@author: USER
"""

def maximum_subarray(array):
    max = 0
    starting_index = 0
    ending_index = 0
    for i in range(len(array)):
        sum = 0
        for j in range(i, len(array)):
            sum = sum + array[j]
            if sum > max:
                max = sum
                starting_index = i
                ending_index = j
                
    return max, starting_index, ending_index

def main():
    array = [-2,1,-3,4,-1,2,1,-5,4]

    max, starting_index, ending_index = maximum_subarray(array)

    print(max)

    print(array[starting_index:ending_index + 1:1])
    
if __name__ == "__main__":
    main()


