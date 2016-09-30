#!/usr/bin/python

#source: http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html
'''
In order to implement an unordered list, we will construct what is commonly 
known as a linked list.
Recall that we need to be sure that we can maintain the relative positioning 
of the items. 
However, there is no requirement that we maintain that posistioning in 
contiguous memory. 

It is important to note that the location of the first item of the list must
be specified. Once we know where the first item is, the first item can tall us
where the second is, and so on. The external reference is often referred to as the head
of the list. Similarly, the last item needs to known that there is no next item. 

The basic building block for the linked list implementation is the node.
Each node object must hold at least two piecies of information. 
First, the node must contain the list item itself. We will call this the data 
field of the node. 
In addition, each node must hold a reference to the next node. 
The Node class also includes the usual methods to access and modify the data
and the next reference
'''

class Node:

	# constructor
	def __init__(self, initData, position = 0):

		# the data item of the node
		self.data = initData
		# A reference to next node
		# A reference to None will denote the fact that
		# there is no next node. 
		# Note in the constructor that a node is initially created with 
		# next set to None.
		self.next = None


	# get data
	def getData(self):
		return self.data

	# get a referece to next node
	def getNext(self):
		return self.next

	# set data
	def setData(self, newData):
		self.data = newData

	# set next node
	def setNext(self, newNext):
		self.next = newNext



'''
The unordered list will be built from a collection of nodes,
each lined to the next by explicit references.
As long as we know where to find the first node (containing the first item),
each item after that can be found by successivelly folloing the next links.
With this in mind, the UnOrderedList class must maitain a reference to the fist node.

It is important to note that the list class itself does not contain any node objects.
Instead it contains a single reference to only the first node in the linked structure.
'''

class UnOrderedList:

	# constructor
	def __init__(self):
		self.head = None


	# checks to see if the head of the list 
	# is a reference to None. 
	# the result of the boolean expression self.head == None
	# will only be true if there are no nodes in the linked list.

	def isEmpty(self):
		return self.head == None



	# How do we get items into our list !
	# We need to implement the add method. 
	# However, before we can do that, we need to address the important question
	# of where in the linked list to place the new item. 
	# Since this list is unordered, the specific location of the new item with
	# respect to the other items already in the list is not important.
	# The new item can go anywhere.
	# With that in mind, it makes sense to place the new item in the easiest location possible
	# Recall that the linked list structure provides us with only one entry point, the head of the lsit.
	# All of the other nodes can only be reached by accessing the first node and then 
	# following next links. 
	# This means that the easiest place to add the new node is right at the head, or beginning, 
	# of the list. 
	# In other words, we will make the new item the first item of the list and the existing
	# items will need to be linked to this new first item so that they follow.

	# A list to store temp nodes


	def add(self, item):

		# creates a new node
		temp = Node(item)

		# linking the new node into the existing struture.
		# changes the next reference of the new node to refer to the old first node 
		# of the list.
		temp.setNext(self.head)

		# update the head
		self.head = temp


	def size(self):

		# External reference current is initialized to the head of the list
		current = self.head

		# At the start of the process we have not seen any nodes so the count is set to 0
		count = 0

		# implement the traversal.
		# As long as the current reference has not seen the end of the list (None)
		while current != None:

			# Add 1 to number of nodes
			count = count + 1
		# We move current along to the next node 
			current = current.getNext()

		return count

	def search(self, item):

		# the traversal is initialize to start at the head of the list
		current = self.head

		# A boolean variable called found to rememeber
		# whether we have located the item we are searching for
		# Since we have not found the item at the start of the traversal
		# found can be set to False
		found = False 

		# As long as there are more nodes to visit and we have not found the item
		# we are looking for, we countinue to check the next node
		while current != None and not found :
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()

		return found

 	def remove(self, item):
 		current = self.head
 		previous = None
 		found = False

 		while not found:
 			if current.getData() == item:
 				found = True
 			else:
 				previous = current
 				current = current.getNext()


 		if previous == None:
 			self.head = current.getNext()
 		else:
 			previous.setNext(current.getNext())

 	def show(self):
 		print("Show list data: ")
 		current = self.head
 		while current != None:
 			print(current.getData())
 			current = current.getNext()




myList = UnOrderedList()

# add nodes to the list
myList.add(0)
myList.add(1)
myList.add(2)
myList.add(3)

myList.show()



