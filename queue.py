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


 
