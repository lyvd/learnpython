#!/usr/bin/python

'''
Doubly Linked List is a variation of Linked list in which navigation is possible
in both ways either forward and backward easily as compared to Single Linked List.
'''

# A node class
class Node(object):

	# Constructor
	def __init__(self, data, prev, nextnode):

		# object data
		self.data = data

		# previous node
		self.prev = prev

		# next node
		self.next = nextnode

# Dobule list of nodes
class DoubleList(object):

	def __init__(self):
		self.head = None
		self.tail = None
	
	# append a node to the list
	def append(self, data):

		tail = Node(data, None, None)
		# create a new node
		new_node = Node(data, None, None)

		# if node is the last node
		if self.head is None:

			# head = tail = new node
			self.head = self.tail = new_node

		else:
			# point prev link of new node to tail
			new_node.prev = self.tail

			# create a new node
			new_node = None

			# point next link of tail to new node
			self.tail.next = new_node

			# tail is the new node
			self.tail = new_node

	# Show nodes
	def show(self):
		print("Showing list data:")

		# external variable point to head
		current_node = self.head

		# loop until the end of the list
		while current_node is not None:
			print(current_node.data) if hasattr(current_node.prev, "data") else None,
			print(current_node.data),
			print(current_node.next.data) if hasattr(current_node.next, "data") else None

			current_node = current_node.next

d = DoubleList()

d.append(5)
d.append(6)
d.append(50)
d.append(30)

d.show()




