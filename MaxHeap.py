# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 18:57:51 2019

@author: user_PC
"""

class MaxHeap:
	def __init__(self, items=[]):
		self.heap = [-float('Inf')]
		for i in items:
			self.heap.append(i)
			self.__floatUp(len(self.heap) - 1)

	def push(self, data):
		self.heap.append(data)
		self.__floatUp(len(self.heap) - 1)

	def peek(self):
		if self.heap[1]:
			return self.heap[1]
		else:
			return False
			
	def pop(self):
		if len(self.heap) > 2:
			self.__swap(1, len(self.heap) - 1)
			max = self.heap.pop()
			self.__bubbleDown(1)
		elif len(self.heap) == 2:# один элемент в куче
			max = self.heap.pop()
		else: # пустая куча
			max = False
		return max

	def __swap(self, i, j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

	def __floatUp(self, index):
		parent = index//2#целочисленное деление
		if index <= 1:
			return
		elif self.heap[index] > self.heap[parent]:
			self.__swap(index, parent)
			self.__floatUp(parent)# продолжаем, пока не пройдем снизу вверх

	def __bubbleDown(self, index):
		left = index * 2
		right = index * 2 + 1
		largest = index
		if len(self.heap) > left and self.heap[largest] < self.heap[left]:
			largest = left
		if len(self.heap) > right and self.heap[largest] < self.heap[right]:
			largest = right
		if largest != index:# свапаем до тех пор пока не начнет совпадать  
			self.__swap(index, largest)
			self.__bubbleDown(largest)# опускаем ниже меньший элемент

m = MaxHeap([2, 3, 15, 890])
m.push(18)
m.push(12)
print(str(m.pop()))
print(str(m.pop()))
m.push(12)
print(str(m.pop()))
