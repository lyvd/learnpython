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
	t = root.pop(1)
