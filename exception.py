
'''
A finally clause is always executed before leaving the try statement, 
whether an exception has occurred or not. When an exception has occured in the try
clause and has been handled by an except cluase (or it has occured in an except or else
clause), it is re-raised after the finally clause has been executed.
'''
def divide(x, y):
	try:
		result = x / y
	except ZeroDivisionError:
		print('division by zero')
	else:
		print('result is %d'  % result)
	#finally:
	#	print("executing finally clause")

print(divide(2, 1))
print("\n")
print(divide(2, 0))
print("\n")
print(divide("2", "1"))