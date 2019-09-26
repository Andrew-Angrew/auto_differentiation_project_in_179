import random
from math import *

def optimize(f):
    now = (0, 0)
    way = [now]
    r = 100
    for i in range(17900):
        x = random.random()
        l = random.uniform(0, r)
        y = sqrt(1 - x * x)
        p1 = (now[0] + x, now[1] + y)
        p2 = (now[0] + x, now[1] - y)
        if f(p1) < f(p2):
            p0 = p1
        else:
            p0 = p2
        if f(p2) < f(now):
            now = p2
            way.append(now)
        r = max(1, r - 0.5)
    return way
