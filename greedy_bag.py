# -*- coding: utf-8 -*-
"""
задача о жадном наполнении рюкзака предметами, 
охарактеризованными натуральными числами
Sample Input:

3 50 - число предметов и емкость
60 20 - стоимость и масса первого предмета
100 50
120 30

Sample Output:

180 0 - сколько своровали и оставшее место в рюкзаке
"""
import sys


def main():
    reader = (tuple(map(int,x.split())) for x in sys.stdin)
    items, capacity = next(reader)
    all_objects = list(reader)
    
    all_objects = [(x/y, y) for x,y in all_objects]
    all_objects.sort(key = lambda x: -x[0])    
    current_weight_of_bag = capacity
    price_of_bag = 0   
    
    for weighted_price, weight in all_objects:
        if weight <= current_weight_of_bag: 
            current_weight_of_bag -= weight
            price_of_bag += weighted_price*weight
        else:
            price_of_bag += weighted_price*current_weight_of_bag
            current_weight_of_bag -= current_weight_of_bag
    print(price_of_bag, (capacity-current_weight_of_bag))        

if __name__ == '__main__':
    main()