#!/usr/bin/python

import threading 
import time

class myThread(threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter

	def run(self):
		print("Starting " + self.name)
		# Get lock to synchronize threads
		threadLock.acquire()
		print_time(self.name, self.counter, 3)
		# Free lock to release next thread
		threadLock.release()

def print_time(threadName, delay, counter):
	while counter:
		time.sleep(delay)
		print