#!/usr/bin/python

# Queue module allows you to create a new queue object that can hold a 
# specific number of items 

# using queue
import Queue
import threading
import time

exitFlag = 0

# Create a subclass of Thread 
class myThread(threading.Thread):
	# constructor
	def __init__(self, threadID, name, q):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.q = q

	def run(self):
		print("Starting " + self.name)
		process_data(self.name, self.q)
		print("Existing " + self.name)

def process_data(threadName, q):
	# while exitFlag is 0
	while not exitFlag:
		# create a new lock, the first argument of acquire method is 
		# 0 which indicates that the lock can not be acquired
		queueLock.acquire()
		# if workQueue is not empty
		if not workQueue.empty():
			# removes and get an item from the queue
			data = q.get()
			# free lock to release next thread
			queueLock.release()
			print("%s processing %s" %(threadName, data))
		else:
			queueLock.release()
		time.sleep(1)


# a list of thread name
threadList = ["Thread-1", "Thread-2", "Thread-3"]

nameList = ["One", "Two", "Three", "Four", "Five"]

# create a threading lock to synchronize threads
queueLock = threading.Lock()

# maximum number of items in a queue
workQueue = Queue.Queue(10)

# an thread list
threads = []

# initialize thread ID
threadID = 1

# create new threads
for tName in threadList:

	# create a myThread instance
	thread = myThread(threadID, tName, workQueue)

	# start a new thread
	thread.start()

	# store the current thread
	threads.append(thread)

	# increase thread ID
	threadID += 1

# Fill the queue
# force threads run synchronously
# blocking is 0 indicates that the thread 
#returns immediately with a 0 value if the lock cannot be acquired 
#and with a 1 if the lock was acquired 
queueLock.acquire()

# loop over the nameList
for word in nameList:

	# put each item in the list to queue
	workQueue.put(word)

# the queue was filled with the items
# then release the lock

# Wait for queue to empty

while not workQueue.empty():
	pass

# Notify theads it's time to exit
exitFlag = 1

# Wait for all threads to complete
# loop over thread list
for t in threads:
	t.join()

print("Exiting Main Thread")





