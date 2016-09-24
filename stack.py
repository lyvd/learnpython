# source: http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaStackinPython.html
# This file demonstrates the implementation of Stack data stucture in Python.
# Stack is also a mechanism to store data. It operates base on LIFO (Last In First Out), the first item is added
# is the last item is poped
# A stack can be consdiered as a list class with the top of the stack is the last item of the list.
# If you want to push an item to the stack, we append this item to the list. 
# If you want to pop an item from the the stack, we pop this item from the list.

# Declare a Stack class
class Stack:
	def __init__(self):
		# construct a list 
		self.items = []

	# whether a stack (list) is empty
	def isEmpty(self):
		self.items == []

	# add an item to the stack
	def push(self, item):
		self.items.append(item)

	# pop an item from the stack
	def pop(self):
		self.items.pop()

	# get size of a stack (list)
	def getSize(self):
		return len(self.items)

	# display items in the Stack
	def getItems(self):
		for i in self.items:
			print(i)
		

# Create an instance of a Stack class
c = Stack()

# push a number to the stack
c.push(3)

# push a string to the stack
c.push("Hello")

# get items in Stack
c.getItems()

# pop an item form the stack
c.pop()

# get items in Stack
c.getItems()




