# -*- coding: utf-8 -*-
"""
с этим кодом енкодинга по хаффману еще предстоит разобраться
на вод строка символов
на выходе 1 и 0. кодирование экономично,
в том смысле что на наиболее часто встречающиеся символы код кратчайший
"""

import heapq
from collections import Counter, namedtuple

class Node(namedtuple('Node', ['left', 'right'])):
    def walk (self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')

        
class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'

        
def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))  
           
    heapq.heapify(h)  
    
    count = len(h)       
    while len(h)>1:
        freq1, _count1,left = heapq.heappop(h)
        freq2, _count2,right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    [(_freq, count, root)] = h
    code = {}
    root.walk(code, "")
    return(code)
           
def main():
    if __name__ == '__main__':
        s = 'abca'#input()
        code = huffman_encode(s)
        encoded = ''.join(code[ch] for ch in s)
        print(len(code), len(encoded))
        for ch in sorted (code):
            print('{}: {}'.format(ch, code[ch]))
        print(encoded)  

main()