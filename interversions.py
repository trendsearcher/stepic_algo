# -*- coding: utf-8 -*-
"""
подсчет числа инверсий в данном неотсортированном списке.
"""
import sys
input = sys.stdin #расскомментировать при сдаче задачи в системе
lena = int(input.readline())# число тотрезков
a = (input.readline())
a = (list(map(int, a.split(' '))))# число тотрезков

# число тотрезков

def invertions_in_even_list (a, inversions = 0):   
    '''считает число инверсий в списке четной длины, например:
       в [8,7,6,5,4,3,2,1] n*(n-1)/2 = 28 инверсий'''    
    while len(a) > 1:
        i = 0
        j = 1
        while i < len(a) and j < len(a):
            if type(a[i]) == int: #список чисел
                aa = a[i]
                bb = a[j]
                if bb < aa:
                    inversions += 1
                    parts_to_merge = [bb, aa]    
                else:
                    parts_to_merge = [aa, bb]
            else:  #список списков чисел
                aa = a[i]
                bb = a[j]
                maxjj = maxii = len(aa)
#                maxjj = len(bb)
                jj = 0
                while jj < maxjj:
                    ii = 0
                    while ii < maxii:
                        if bb[jj] < aa[ii]:
                            inversions += (maxii - ii)
                            break
                        else:
                            ii += 1
                    jj += 1 
                parts_to_merge = sorted(aa+bb)  
            
            a[i] = parts_to_merge
            a.remove(a[j])
            i+=1
            j+=1
    return(inversions)        



if lena%2 == 0:            
    print(invertions_in_even_list (a, inversions = 0))
else:
    additive = 0
    fst = a.pop(0)
    for i in a:
        if i < fst:
            additive += 1
    print(additive+invertions_in_even_list (a, inversions = 0))
#















#def merge_sort(A):
#    merge_sort2(A, 0, len(A)-1) # нельзя задавать атрибуты функции внутри 
#    
#def merge_sort2(A, first, last):
#    if first < last:
#        middle = (first + last)//2
##        print(1, middle)
#        merge_sort2(A, first, middle)
##        print(2, middle)
#        merge_sort2(A, middle+1, last)
##        print(3, middle)
#        merge(A, first, middle, last)
##        print(4, middle)
#		
#def merge(A, first, middle, last):
#    L = A[first:middle+1]
#    R = A[middle+1:last+1]
#    L.append(sys.maxsize)
#    R.append(sys.maxsize)
#    i = j = 0
#    
#    for k in range (first, last+1):
#        if L[i] <= R[j]:
#            A[k] = L[i]
#            i += 1
#        else:
#            A[k] = R[j]
#            print('d' *(len(L)- i-1)*(len(R)- j - 1), end = '')
#            j += 1
#            
#
#A = [1, 2, 5, 4]
#merge_sort(A)
#print(A)
    
    
    
    
    
    
    
    