# source http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaQueueinPython.html
# I learn the implementation of Queue data structure in Python
# As far as you know, Queue is a mechanism to store data. It works base on FIFO (First In First out)
# It means that, the first item is put in the queue is the first item is pop

''' 

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

'''

'''
The Queue module provides a first-in, first-out  (FIFO) data structure for 
multi-threaded programming. It can be used to pass messages or other data 
safely between producer and consumer threads. Locking is handled for the caller,
so many threads can work with the same Queue instance safely. The size of a Queue 
(the number of elements it contains) may be restricted to throttel memory usage
or processing'''

import Queue

'''
# Create a Queue instance
q = Queue.Queue()

for i in range(5):
    # put data in queue
    q.put(i)

while not q.empty():
    print(q.get())
'''
# This example uses a single thread to illustrate that elements are removed from the queue
# in the same order they are inserted

'''
In constrast to the standard FIFO implementation of Queue, the LifoQueue uses last-in 
first-out (LIFO) ordering (normally associated with a stack data structure)

'''

'''
q = Queue.LifoQueue()

for i in range(5):
    q.put(i)


while not q.empty():
    print(q.get())

print

'''

'''
Sometimes, the processing order of the items in a queue needs to be based on 
characteristics of those items, rather than just on the order in which they 
are created or added to the queue. 
For example, print jobs from the payroll department may take precedence
over a code listing printed by a developer. PriorityQueue uses the sort
order the contents of the queue to decide which to retrieve
'''

import threading

class Job(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print("New job: ", description)
        return

    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

q = Queue.PriorityQueue()

q.put(Job(3, 'Midd-level job'))
q.put(Job(10, 'Low-level job'))
q.put(Job(1, 'Important job'))

def process_job(q):
    while True:
        next_job = q.get()
        print("Processing job:", next_job.description)
        q.task_done()

workers = [threading.Thread(target = process_job, args = (q, )), 
           threading.Thread(target = process_job, args = (q, )),]

for w in workers:
    w.setDaemon(True)
    w.start

q.join()