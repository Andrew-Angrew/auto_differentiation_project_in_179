import random
from math import *

def optimize(f):
    def my_key(a):
        return f(a)
    now = (0, 0)
    way = [now]
    r = 100
    for i in range(17900):
        x = random.random()
        l = random.uniform(0, r)
        y = sqrt(1 - x * x)
        p1 = (now[0] + x, now[1] + y)
        p2 = (now[0] + x, now[1] - y)
        p3 = (now[0] - x, now[1] + y)
        p4 = (now[0] - x, now[1] - y)
        p0 = min(p1, p2, p3, p4, key=my_key)
        if f(p0) < f(now):
            now = p0
            way.append(now)
        r = max(1, r - 0.5)
    return way
