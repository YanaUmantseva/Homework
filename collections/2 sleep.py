from time import sleep

def dec(func):
    def wrap(*args, **kwargs):
        sleep(2)
        return func(*args, **kwargs)
    return wrap

@dec
def calc(a, b):
    return a **b
@dec
def calc_2(x,y,z):
    return x*y**z

print(calc(2, 3))
print(calc_2(4, 3, 2))