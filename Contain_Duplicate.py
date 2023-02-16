# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 20:27:42 2022

@author: USER
"""

def containDuplicate(array):
    for i in range(len(array)):
        count = 0
        for j in range(len(array)):
            if array[i] == array[j]:
                count += 1
        if (count >= 2):
            return True
    return False

def main():
    array = [1,2,3,2]
    print(containDuplicate(array))
    
if __name__ == "__main__":
    main()