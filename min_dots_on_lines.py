# -*- coding: utf-8 -*-
"""
покрытие отрезков минимальным числом точек

"""
#import string
#import sys
input = open('C:\\Users\\user_PC\\Desktop\\otrezki.txt', 'r') #расскомментировать решая задачу локально
#input = sys.stdin //расскомментировать при сдаче задачи в системе

S = [] # список списков [начало отрезка, конец отрезка]
n = int(input.readline())# число тотрезков
for i in range(1,n+1):
  x,y = map(int, input.readline().split(' '))
  S.append([x,y])

S.sort(key=lambda x: x[1])  
print(S)
intervals = S
n = len(S)
points = []
current = None

for i in intervals:
    if current and i[0] <= current[1]:
        continue
    current = i
    points += [i[1]]

print('число точек {}'.format(len(points)))
for p in points:
    print(p, end = ' ')
#

