# source http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaQueueinPython.html
# I learn the implementation of Queue data structure in Python
# As far as you know, Queue is a mechanism to store data. It works base on FIFO (First In First out)
# It means that, the first item is put in the queue is the first item is pop 

class Queue:
    # construction
    def __init__(self):
        # this queue contains a list
        self.items = []

    # whether the list is empty ?
    def isEmpty(self):
        return self.items == []

    # insert an item into a list
    def enqueue(self, item):
        self.items.insert(0, item)

    # remove an item from a list
    def dequeue(self):
        return self.items.pop()

    # get size of a list
    def size(self):
        return len(self.items)

    # get items in the list
    def getItems(self):
        for i in self.items:
            print(i)

# Create a queue
q = Queue()

# add a number into the queue
q.enqueue(4)

# add a string into the queue
q.enqueue("dog")

# add a boolean value into the queue
q.enqueue(True)

# get size of the list into the queue
print("%d" %(q.size()))

# get items of the list into the queue
q.getItems()

# remove an item in the list
q.dequeue()
 
# display items after removing 
q.getItems()
