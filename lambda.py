#!/usr/bin/python

# Lambda is a construct that supports the creation of anonymous functions
# Lamda function does not have a return.

# lambda function with a single variable
import struct
g = lambda x: x**2
print g(8)

# We cannot use print or raise function in lambda
h = lambda x: True if x > 10 else False
result = h(12)
print(result)

# two arguments
def make_incrementor(n): return lambda x: x + 2*n

f = make_incrementor(3)
print(f(4))

print make_incrementor(3)(4)

# lambda with filter

foo = [1, 3, 4, 5, 2, 4, 11, 22, 3 ,4, 6]

# filter values greater than 5
print filter(lambda x : x - 5 > 0 , foo)

# do another way by using if condition
print filter(lambda x : True if x > 5 else False, foo)

# lambda with map, map function is used to convert our list
# The given function is called for every element in the original list,
# and a new list is created which contains the return values from
# our lambda function.
print map(lambda x: 2*x + 10, foo)

# lambda with reduce, the "worker function" for this one must accept two
# arguments. The function is called with the first two elements from the list
# then with the result of that call adn the third element, and so on, until all of 
# of the list elements have been handled. 

print reduce(lambda x, y: x * y, foo)

pck32 = lambda x: struct.pack('I', x)
print pck32(0x00014)