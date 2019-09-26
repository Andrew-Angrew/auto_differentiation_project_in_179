from optimize import optimize




def f1(x, y):
    return x + y

def f2(x, y):
    return x

def check_optimizer(f):
    def check(a, b):
        return f(a[0], a[1]) > f(b[0], b[1])
    
    
    a = optimize(f)
    for i in range(len(a) - 1):
        if not check(a[i], a[i + 1]):
            raise ValueError("something is wrong")
    if f(a[0][0], a[0][1]) - f(a[-1][0], a[-1][1]) <= 5:
        raise ValueError("it is a bad optimizer, Mitya luzer")
    
check_optimizer(f1)
check_optimizer(f2)