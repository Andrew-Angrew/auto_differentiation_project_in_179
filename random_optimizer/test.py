from optimize import optimize




def f1(x):
    return x[0] + x[1]

def f2(x):
    return x[0]

def check_optimizer(f):
    def check(a, b):
        return f(a) > f(b)
    
    
    a = optimize(f)
    for i in range(len(a) - 1):
        if not check(a[i], a[i + 1]):
            raise ValueError("something is wrong")
    if f(a[0]) - f(a[-1]) <= 5:
        raise ValueError("it is a bad optimizer, Mitya luzer")
    
check_optimizer(f1)
check_optimizer(f2)