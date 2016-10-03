#!/usr/bin/python
# source: http://interactivepython.org/runestone/static/pythonds/Trees/ListofListsRepresentation.html
# construct a tree as list of lists
# the root node is the fist item, the second item is the left subtree
# the third item is the right subtree
myTree = ['a',   #root
      ['b',  #left subtree
       ['d', [], []],
       ['e', [], []] ],
      ['c',  #right subtree
       ['f', [], []],
       [] ]
     ]

# display the tree
print(myTree)

# the root node
print(myTree[0])

# the left subtree
print(myTree[1])

# the right subtree
print(myTree[2])

# a function to construct a tree
def BinaryTree(r):
	return [r, [], []]

def insertLeft(root, newBranch):

	# check the second item is empty or not ?
	t = root.pop(1)

	# if there is something in the second position
	if len(t) > 1:

		# push it down the tree as the left child of the list we are adding
		root.insert(1, [newBranch, t, []])

	# if there is nothing in the second position
	else:

		# insert a new brach with empty subtrees
		root.insert(1, [newBranch, [], []])

# The code for insertRight is similar to insertLeft 

def insertRight(root, newBranch):

	# check the third item is empty or not ?
	t = root.pop(2)

	# if there is something in the third position
	if(len(t) > 1):

		# push it down the tree as the right child of the list we are adding
		root.insert(2, [newBranch, [], t])

	# if there is nothing in the third position
	else:
		root.insert(2, [newBranch, [], []])

# Get root's value
def getRootVal(root):
	return root[0]

# Set root's value
def setRootVal(root, newVal):
	root[0] = newVal

# Get left child
def getLeftChild(root):
	return root[1]

# get right child
def getRightChild(root):
	return root[2]

# Construct a new tree
r = BinaryTree(3)

# display the tree
print(r)

# Add a left child 
insertLeft(r, 4)

# Add a right child
insertRight(r, 5)

#Add a left child
insertLeft(r, 6)

print(r)

