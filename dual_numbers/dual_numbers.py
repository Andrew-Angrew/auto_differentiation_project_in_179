#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import math

# Object of this class describes an expression a + b * epsilon + o(epsilon).
# Define all arithmetic operations 
class DualNumber:
    def __init__(self, a, b=None):
        if b is None and isinstance(a, DualNumber):
            self.a = a.a
            self.b = a.b
        else:
            self.a = a
            self.b = 0 if b is None else b

    # should return self + other
    def __add__(self, other):
        other = DualNumber(other)
        # write your code here

    # should return self - other
    def __sub__(self, other):
        other = DualNumber(other)
        # write your code here

    # should return self * other
    def __mul__(self, other):
        other = DualNumber(other)
        # write your code here

    # should return self / other
    def __truediv__(self, other):
        other = DualNumber(other)
        # write your code here

    # should return self ** power.
    # You can assume that power is a natural number.
    def __pow__(self, power):
        # write your code here
        pass

    # should return -self
    def __neg__(self):
        # write your code here
        pass
    
    # should return abs(self)
    def __abs__(self):
        # write your code here
        pass

    # should return self < other.
    def __lt__(self, other):
        other = DualNumber(other)
        # write your code here

    # should return self == other.
    def __eq__(self, other):
        other = DualNumber(other)
        # write your code here

    # should return self <= other.
    def __le__(self, other):
        other = DualNumber(other)
        # write your code here

#auxilliaty methods:
    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return DualNumber(other).__sub__(self)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rtruediv__(self, other):
        return DualNumber(other).__truediv__(self)

    def __str__(self):
        return "{}{:+}epsilon".format(self.a, self.b)

    def __repr__(self):
        return str(self)

def sin(x):
    if isinstance(x, DualNumber):
        return DualNumber(math.sin(x.a), math.cos(x.a) * x.b)
    return math.sin(x)

def cos(x):
    if isinstance(x, DualNumber):
        # write your code here
        pass
    return math.cos(x)

def exp(x):
    if isinstance(x, DualNumber):
        # write your code here
        pass
    return math.exp(x)

def log(x):
    if isinstance(x, DualNumber):
        # write your code here
        pass
    return math.log(x)

def D(f):
    def f_derivative(x):
        x = DualNumber(x, 1)
        return f(x).b
    return f_derivative


