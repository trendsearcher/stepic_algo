# -*- coding: utf-8 -*-
"""
В первой строке задано два целых числа 1≤n≤50000 и 1≤m≤50000 — количество отрезков
и точек на прямой, соответственно. Следующие n строк содержат по два целых числа 
ai и bi (ai≤bi) — координаты концов отрезков. Последняя строка содержит m целых 
чисел — координаты точек. Все координаты не превышают 10 000 000. Точка 
считается принадлежащей отрезку, если она находится внутри него или на границе. 
Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.
"""
'''считаем с помощью бинарного поиска в отсортированном списке левые концы
отрезков, которые не правее точки и вычитаем правые концы, которые левее точки
время примерно O(nlogn)+O(nlogn)+O(mlogn)+O(mlogn) '''
import sys
import bisect

def index_left(a, x):
    'на вход идет список и число.возвращает количество элементов слева от числа'
    i = bisect.bisect_left(a,x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return(bisect.bisect(a, x))

reader = (tuple(map(int,x.split())) for x in sys.stdin)
lines, dots = next(reader)
rest = list(reader)
all_lines = rest[:-1]
all_dots = rest[-1]    
    
#all_lines = [(0,3),(1,3),(2,3),(3,4),(3,5),(3,6)]
#all_dots = (1,2,3,4,5,6)
#Ответ 2 3 6 3 2 1

starts = [x[0] for x in all_lines]
starts.sort()
ends = [x[1] for x in all_lines]
ends.sort()

for dot in all_dots:
    counter = bisect.bisect(starts, dot) - index_left(ends, dot)
    print(counter, end = ' ')    
