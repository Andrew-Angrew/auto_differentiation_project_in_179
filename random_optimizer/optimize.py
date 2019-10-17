import random
import math

def optimize(f, iterations=1000):
    now = (0, 0)
    way = [now]
    r = 100

    for i in range(iterations):
        angle = random.uniform(0, math.pi)
        x, y = now
        candidates = [
            (x + r * math.cos(angle), y + r * math.sin(angle)),
            (x - r * math.cos(angle), y - r * math.sin(angle))
        ]
        best_point = min(candidates, key=f)
        if f(best_point) < f(now):
            now = best_point
            way.append(now)
        else:
            r /= 2
    return way
