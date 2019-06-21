# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 17:28:14 2019

@author: user_PC
"""
#import sys
input = open('C:\\Users\\user_PC\\Desktop\\otrezki.txt', 'r') #расскомментировать решая задачу локально
#input = sys.stdin //расскомментировать при сдаче задачи в системе

def binary_search_recursive(arr, elem, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start > end:
        return (-1)
    mid = (start + end) // 2
    if elem == arr[mid]:
        return (mid + 1)
    elif elem < arr[mid]:
        return binary_search_recursive(arr, elem, start, mid-1)
    else:
       return binary_search_recursive(arr, elem, mid+1, end)
    
fst = (input.readline())# число тотрезков
fst_list = (list(map(int, fst.split(' '))))[1:]

snd = (input.readline())# число тотрезков
snd_list = (list(map(int, snd.split(' '))))[1:]

for item in snd_list:
    print(binary_search_recursive(fst_list, item), end = ' ')


