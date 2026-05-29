'''
Modules:
-->A module in python is a file taht contains python code such as
variables
functions
classes
statements

two types of modules:--
user-define
built- in

def add(a,b):
    return  a+b
def sub(a,b):
    return  a-b

import math
print(math.sqrt(25))

print(math.factorial(10))
print(math.pow(2,5))


from math import sqrt
print(sqrt(25))

import math as i
print(i.factorial(10))
print(i.pow(2,5))

import os-->it is used to communicate with the system"
os.mkdir("Some_python")

import os
os.rmdir("chatgpt.txt")

import sys
print(sys.version)

import sys
print(sys.version)
print(sys.exit)
print(sys.path)

import random
print(random.randint(1000,9999))

from collections  import Counter
data = ['a','b','c','d']
counter = Counter(data)
print(counter)
'''

from collections  import Counter,defaultdict
data = ['a','b','c','d']
counter = Counter(data)
print(counter)

dd =defaultdict(int)
dd['missing'] +=1
print(dd['missing'])
print(dd)





















