# -*- coding: utf-8 -*-
"""
В первой строке даны целое число 1≤n≤105 и массив A[1…n] из n различных 
натуральных чисел, не превышающих 109, в порядке возрастания, во второй — 
целое число 1≤k≤105 и k натуральных чисел b1,…,bk, не превышающих 109. Для 
каждого i от 1 до k необходимо вывести индекс 1≤j≤n, для которого A[j]=bi,
 или −1, если такого j нет.
 
 Sample Input:
5 1 5 8 12 13
5 8 1 23 1 11

Sample Output:
3 1 -1 1 -1
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


