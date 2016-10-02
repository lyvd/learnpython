#!/usr/bin/python
# source : http://www.tutorialspoint.com/python/python_multithreading.htm
# using thread
import threading
import time

'''
# Define a function for the thread
def print_time(threadName, delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		print("%s: %s" %(threadName, time.ctime(time.time())))

# Create two threads as follows
try:
	# spawn a new thread 
	thread.start_new_thread(print_time, ("Thread-1", 2 ))
	thread.start_new_thread(print_time, ("Thread-2", 4 ))
except Exception as e:
	raise e

'''

# This method 

'''
The simplest way to use a Thread is to instantiate it with a target function and 
call start() to let it begin working
'''

'''
def worker(num):
	#threading worker funciton 
	num = num + 1
	print('Num : %d' % num)
	return

threads = []

for i in range(5):
	t = threading.Thread(target = worker, args = (i, ))
	threads.append(t)
	t.start()
'''
import threading
import time
import logging

'''
# first worker
def worker():

	# starting time
	print(threading.currentThread().getName() +  ' Starting')
	time.sleep(2) 

	# existing time
	print(threading.currentThread().getName() + ' Existing')

# second worker
def my_service():

	# starting time
	print(threading.currentThread().getName() + ' Starting')
	time.sleep(3)

	# existing time
	print(threading.currentThread().getName() + ' Existing')

# Assign threads to variables
t = threading.Thread(name = 'my_service', target = my_service)
w = threading.Thread(name = 'worker', target = worker)
w2 = threading.Thread(name = 'worker_1', target = worker)

# Start first thread
w.start()
w2.start()
t.start() 
'''

'''
logging.basicConfig(
	level = logging.DEBUG,
	format = '[%(levelname)s] (%(threadName) - 10s) %(message)s',
	)

# first worker
def worker():
	logging.debug('Starting')
	time.sleep(2)
	logging.debug('Existing')

# second worker
def my_service():
	logging.debug('Starting')
	time.sleep(3)
	logging.debug('Existing')

t = threading.Thread(name = 'my_service', target = my_service)
w = threading.Thread(name = 'worker', target = worker)
w2 = threading.Thread(name = 'worker_1', target = worker)

# Start first thread
w.start()
w2.start()
t.start() 

'''

'''
Up to this point, the example programs have implicitly waited to exit until all threads have completed their work
Programs somtimes spawn a thead as a daemon that runs without blocking the main program from existing.
Using daemon threads is useful for services where there may not be an easy way to interupt the thread, or where
letting the thread die in the middle of its work does not lose or corrupt data.
To mark a thread as a daemon, call its setDaemon() method with True. 
'''
'''
logging.basicConfig(
	level = logging.DEBUG,
	format = '[%(levelname)s] (%(threadName) - 10s) %(message)s',
	)

# first worker
def daemon():
	logging.debug('Starting')
	time.sleep(4)
	logging.debug('Existing')

# Start a daemon
d = threading.Thread(name = 'daemon', target = daemon)
d.setDaemon(True)

# second worker
def non_daemon():
	logging.debug('Starting')
	time.sleep(1)
	logging.debug('Existing')


n = threading.Thread(name = 'non daemon', target = non_daemon)
#w2 = threading.Thread(name = 'worker_1', target = worker)

# Start first thread
d.start()
#n.start()
#t.start() 

d.join(10)

print(d.isAlive())
#n.join(3)
#print(n.isAlive())

'''

'''
It is not necessary to retain an explicit handle to all the daemon threads to ensure they
have completed before exiting the main process. enumerate() returns a list of active Thread instances
The list includes the current thread, and since joining the current thread introduce a deadlock situation , it 
must be skipped.
'''
import random

'''
logging.basicConfig(
	level = logging.DEBUG,
	format = '[%(levelname)s] (%(threadName) - 10s) %(message)s',
	)

# first worker
def worker():
	"""thread worker funciton"""

	# get the current thread
	t = threading.currentThread()

	# sleep time
	pause = random.randint(1, 5)

	logging.debug('Sleeping %d', pause)

	time.sleep(pause)

	logging.debug('Ending')

	return

# assign threads
for i in range(3):

	# assign 3 threads
	t = threading.Thread(target = worker)

	# each thread is a deamon
	t.setDaemon(True)

	# start thread
	t.start()

# get main thread
main_thread = threading.currentThread()

# enumerate current threads
for t in threading.enumerate():
	if t is main_thread:
		continue
	logging.debug('joining %s' % (t.getName()))
	t.join()

'''
'''
At start-up, a Thread does some basic initialization and then call its run() method,
which calls the target function passed to the constructor. To create a subclass of Thread,
override run() to do whatever is necessary


'''
logging.basicConfig(
	level = logging.DEBUG,
	format = '[%(levelname)s] (%(threadName) - 10s) %(message)s',
	)
''''
class MyThread(threading.Thread):

	# override run method
	def run(self):
		logging.debug('running')
		return 

for i in range(5):
	t = MyThread()
	t.start()
'''

'''
Because the args and kwargs values passed to Thread constructor 
are saved in private variables using names prefixed with '__',
they are not easily accessed from a subclass. To pass arguments
to a custom thread type, redefine the construtor to save the values
in an instance visible from the subclass
'''

'''
class MyThreadWithArgs(threading.Thread):

	def __init__(self, group = None, target= None, name = None, args = (), 
		kwargs = None, verbose = None):
		threading.Thread.__init__(self, group = group, target = target, name = name, verbose = verbose)

		self.args = args
		self.kwargs = kwargs
		return

	def run(self):
		logging.debug('running with %s and %s' % (self.args, self.kwargs))
		return


for i in range(5):
	t = MyThreadWithArgs(args=(i, ), kwargs = {'a' : 'A', 'b': 'B'})
	t.start()

'''

'''
One example of a reason to subclass Thread is provided by Timer, also include in threading
A Timer starts its work after a delay and can be canceled at any point within that delay time period
'''

'''

def delayed():
	logging.debug('worker running')
	return

t1 = threading.Timer(3, delayed)
t1.setName('t1')

t2 = threading.Timer(3, delayed)
t2.setName('t2')

logging.debug('starting timers')
t1.start()
t2.start()

logging.debug('Waiting before cancelling %s' % t2.getName())
time.sleep(2)

logging.debug('Canceling %s' % (t2.getName()))
t2.cancel()

logging.debug('done')

'''
'''
Although the point of using multiple threads is to run separate operations concurrently,
there are times when it is important to be able to synchronize the operations in two or more threads.
Event objects are a simple way to communicate between threads safely. An Event manages an internal flag
that callers can control with set() and clear() methods. Other threads can use wait() to pause until the flag is set
effectively blocking progress until allowed to continue.
'''