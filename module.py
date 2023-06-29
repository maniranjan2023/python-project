# Module in python: how to call a function in python.

def sum(a,b):
    c= a+b
    return c

def mul(a,b):
    d=a*b
    return d

#method-1 to call a function which defined earlier is described below:

import module
print(module.sum(10,12))

print(module.mul(12,11))

# method-2 to call a function which defined earlier is described below:
from module import sum
print(sum(10,20))

from module import mul
print(mul(10,13))

# method-3 to call a function which defined earlier is given below:
from module import *
print(sum(10,15))
print(mul(15,30))

# method-3 to call a function which defined earlier is given below:
import module as K # here , we store the name module INSIDE K AND below we use K in place of module:
print(K.sum(14,16))
print(K.mul(17,9))






