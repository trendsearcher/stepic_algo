# -*- coding: utf-8 -*-
"""
Дано целое число 1≤n≤103 и массив A[1…n] натуральных чисел, не превосходящих 
2⋅10^9. Выведите максимальное 1≤k≤n, для которого найдётся подпоследовательность 
1≤i1<i2<…<ik≤n длины k, в которой каждый элемент делится на предыдущий 
(формально: для  всех 1≤j<k, A[ij]|A[ij+1]).
Sample Input:
4
3 6 7 12

Sample Output:
3
"""

import sys
#dot_list = list(map(int,list(sys.stdin)[1].split(' ')))
dot_list =[1,2,3,4,5,6, 12, 12]
#dot_list =[1, 3, 5, 6, 9]

b = [1] * len(dot_list)
for i in range(len(dot_list)):
    for j in range(i):
        if dot_list[i] % dot_list[j] == 0 and b[j] +1 > (b[i]):
            b[i] = b[j] + 1

print(max(b))



