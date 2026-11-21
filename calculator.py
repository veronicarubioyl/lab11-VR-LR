"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# https://github.com/veronicarubioyl/lab11-VR-LR.git
# Partner 1: Veronica Rubio
# Partner 2: Lucas Rosen

import math


# First example
<<<<<<< HEAD
def square_root(a):
    if a<0:
        raise ValueError("Cannot take the square root of a negative number")
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a, b)
def add(a, b): 
    return a + b
=======

def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError('division by zero')
    return b/a
def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError('Invalid base or argument for logarithm')
    return math.log(b, a)
def exp(a, b):
    return a ** b
>>>>>>> fdcda45d510b17decbfe08381bd0dc596fba5f35
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def logarithm(a,b):
    if a == 1 or b <= 0 or a <= 0:
        raise ValueError("Invalid base or argument for logarithm")
    return math.log(b, a)
def exponent(a,b):
    return a**b

