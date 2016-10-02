#!/usr/bin/python

'''
subprocess provides an API for creating and communicating with secondary processes.
it is especially good for running programs that produce or consume text, since
the API supports passing data back and forth through standard input and output 
channels of the new process

The subprocess module provides a consitent way to create and work with additional 
processes. The subprocess module defines one class, Popen, and a few wrapper functions 
that use that class. The constructor for Popen takes arguments to set up the new process
so the parent can communicate with it via pipes. It provides all the functionality 
of the other modules and functions it replaces, and more. 
'''
import subprocess

# simple command
subprocess.call('python')
