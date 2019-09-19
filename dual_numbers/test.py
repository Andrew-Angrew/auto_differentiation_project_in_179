#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import numpy as np
from numbers import Number

from dual_numbers import sin, log, cos, exp, D

def approx_der(f, x, eps=1e-5):
    return (f(x + eps) - f(x)) / eps

def ssin(x):
    for i in range(100):
        x = sin(x)
    return x

def sin_plus_cos(x):
    return sin(x) + cos(x)

def sin_mul_cos(x):
    return sin(x) * cos(x)

def sin_div_cos(x):
    return sin(x) / cos(x)

def trivial_function(x):
    return log(exp(x))

def strange_function(x):
    return sin(x + cos(x + sin(x)))

def approx_test(f, start=1, stop=None, N=101, tol=0.001):
    if stop is None:
        stop = start
        start = 0
    x_range = np.linspace(start, stop, N)
    ders = [D(f)(x) for x in x_range]
    assert all(isinstance(der, Number) for der in ders)
    approx_ders = [approx_der(f, x) for x in x_range]
    if not np.allclose(ders, approx_ders, atol=tol):
        print("Fail for function {}".format(f.__name__))
        plt.plot(x_range, ders, label="ders")
        plt.plot(x_range, approx_ders, label="approximate ders")
        plt.legend()
        plt.show()

for f in [sin, cos, log, exp,
          sin_plus_cos, sin_mul_cos, sin_div_cos,
          ssin, trivial_function, strange_function]:
    approx_test(f, 0.1, 1.1)
