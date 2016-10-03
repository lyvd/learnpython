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

# wait_for_event blocks on the call to wait(), which does not return until
# the event status change
'''
def wait_for_event(e):
	"""Wait for the event to be set before doing anything"""
	logging.debug('wait_for_event starting')

	# get event bit

	the wait() method takes an argument representing the number of seconds
	to wait for the event before timing out. It returns a Boolean indicating 
	whether or not the event is set, so the caller knows why wait() returned. 

	event_is_set = e.wait()

	# log info
	logging.debug('event set: %s' % event_is_set)



def wait_for_event_timeout(e, t):
	"""Wait t seconds and then timeout"""

	while not e.isSet():

		event_is_set = e.wait(t)

		logging.debug('event set: %s' % (event_is_set))

		# if event is set
		if event_is_set:
			logging.debug('processing event')
		else:
			logging.debug('doing other work')

# Event thread
e = threading.Event()


t1 = threading.Thread(name = 'block', target = wait_for_event, args = (e,))
#t1.start()
t2 = threading.Thread(name = 'nonblock', target = wait_for_event_timeout, args = (e, 2))

t2.start()

logging.debug('waiting before calling Event.set()')
time.sleep(3)

e.set()

logging.debug('Event is set')
'''
'''
In addition to synchronizing the operations of threads,
it is also important to be able to control access to shared resources to prevent or 
missed data. Python's built-in data structures (lists, dictionaries, etc.) are 
thread-safe as a side effect of having atomic byte-codes for maniplulating them.
Other data structures implemented in Python, or simpler types like integers and 
float, do not have that protection. To guard against simultaneuous access to an object,
use a Lock object.
'''

'''
class Counter(object):

	# constructor
	def __init__(self, start = 0):

		# Create a lock
		self.lock = threading.Lock()

		self.value = start

	def increment(self):
		logging.debug('Waiting for lock')
		self.lock.acquire()
		try:
			logging.debug('Acquired lock')
			self.value = self.value + 1
		finally:
			self.lock.release()

# worker() function increments a Counter instance, which manages 
# a Lock to prevent two threads from changing its internal state at
# the same time. 
def worker(c):
	for i in range(2):
		pause = random.random()
		logging.debug('Sleeping %0.02f' % pause)
		time.sleep(pause)
		c.increment()
	logging.debug('Done')


counter = Counter()

for i in range(2):
	t = threading.Thread(target = worker, args = (counter, ))
	t.start()

logging.debug('Waiting for worker threads')
main_thread = threading.currentThread()

for t in threading.enumerate():
	if t is not main_thread:
		t.join()

logging.debug('Counter: %d' % counter.value)
'''

'''
To find out whether another thread has aquired the lock without holding up
the current thread, pass False for the blocking argument to aquire().
In the next example, worker() tries to aquire the lock three separate times and 
counts how many attempts it has to make to do so. In the meantime, 
lock_holder() cycles between holding and releasing the lock, with short pauses
in each state used to simluate load
'''
'''
def lock_holder(lock):

	logging.debug('Starting')

	while True:
		lock.acquire()

		try:
			logging.debug('Holding')
			time.sleep(0.5)

		finally:
			logging.debug('Not holding')
			lock.release()
		time.sleep(0.5)
	return

def worker(lock):
	logging.debug('Starting')
	num_tries = 0
	num_aquires = 0

	while num_aquires < 3:
		time.sleep(0.5)
		logging.debug('Trying to aquire')
		have_it = lock.acquire(0)

		try:
			num_tries = num_tries + 1
			if have_it:
				logging.debug('Iteration %d: Acquired' % num_tries)
				num_aquires = num_aquires + 1
			else:
				logging.debug('Iteration %d: Not acquired' % num_tries)
		finally:
			if have_it:
				lock.release()
	logging.debug('Done after %d iterations' % num_tries)

lock = threading.Lock()

holder = threading.Thread(target = lock_holder, args = (lock, ), name = 'LockHolder')

holder.setDaemon(True)

holder.start()

worker = threading.Thread(target = worker, args = (lock, ), name = 'Worker')

worker.start()
'''
'''
Normal Lock objects cannot be acquired more than once, even by the same thread.
This limitation introduce undesirable side effects if a lock is accessed by
more than one function in the same call chain
'''

'''
lock = threading.Lock()

print('First try: ',  lock.acquire())
print('Second try: ', lock.acquire())

'''

'''
In a situation where separate code from the same thread needs to 
"reacquire" the lock, use an RLock instead
'''

'''
lock = threading.RLock()
print('First try: ',  lock.acquire())
print('Second try: ', lock.acquire())
'''

'''
Locks as Context Managers
Locks implement the context manager API and are compatible with the
with statement.
Using with removes the need to explicitly aquire and release the lock
'''

'''
def worker_with(lock):
	with lock:
		logging.debug('Lock aquired via with')

def worker_no_with(lock):
	lock.acquire()
	try:
		logging.debug('Lock aquired directly')
	finally:
		lock.release()

lock = threading.Lock()

w = threading.Thread(target = worker_with, args = (lock, ))
nw = threading.Thread(target = worker_no_with, args = (lock, ))

w.start()
nw.start()
'''

'''
Synchronizing Threads
In addition to using Events, another way of synchronizing threads is 
through using a Condition object. Because the Condition uses a Lock,
it can be tied to a shared resource, allowing multiple threds to wait for the resource 
to be updated.
In this example, the consumer() threds wait for the Condition to be set before continuting
The producer() thread is responsible for setting the condition and notifying
the other threads that they can continue
'''

def consumer(cond):
	"""Wait for the condition and use the resource"""
	logging.debug("Starting consumer thread")
	t = threading.currentThread()

	with cond:
		cond.wait()
		logging.debug('Resource is available to consumer')

def producer(cond):
	"""Set up the resource to be used by the consumer"""
	logging.debug("Starting producer thread")

	with cond:
		logging.debug("Making resource available")
		cond.notifyAll()

condition = threading.Condition()

c1 = threading.Thread(name = 'c1', target = consumer, args = (condition, ))
c2 = threading.Thread(name = 'c2', target = consumer, args = (condition, ))
p = threading.Thread(name = 'p', target = producer, args = (condition, ))

c1.start()

time.sleep(2)

c2.start()

time.sleep(2)

p.start()