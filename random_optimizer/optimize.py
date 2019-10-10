import random
import math

def optimize(f, iterations=1000):
    now = (0, 0)
    way = [now]
    r = 100

    def random_vector():
        angle = random.uniform(0, math.pi)
        return (r * math.cos(angle), r * math.sin(angle))

    for i in range(iterations):
        candidates = [random_vector() + now for i in range(4)]
        best_point = min(candidates, key=f)
        if f(best_point) < f(now):
            now = best_point
            way.append(now)
        else:
            r /= 2
    return way
