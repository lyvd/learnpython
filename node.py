#!/usr/bin/python

# Create a class which presents a node
class BinaryTree:
	def __init__(self, rootObj):
		# root node
		self.key = rootObj

		# left node
		self.leftChild = None
		self.rightChild = None

	# Insert a left node to a tree 
	def insertLeft(self, newNode):
		# if there is no left node
		if self.leftChild == None:
			self.leftChild == BinaryTree(newNode)
		# if there is an existing left node
		# adding the existing node to the node we are adding
		else:
			t = BinaryTree(newNode)	
			t.leftChild = self.leftChild
			self.leftChild = t