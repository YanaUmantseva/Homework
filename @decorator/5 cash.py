def cache3(func):
    cache = []
    counter = 0

    def wrap(*args):
        nonlocal counter
        if counter < 3:
            result = cache[counter] if counter < len(cache) else func(*args)
            counter += 1
            return result
        else:
            result = func(*args)
            cache = [result]
            counter = 1
            return result

    return wrap

@cache3
def function():
    print(' сложные вычисления...')
    return 42

print(function())
print(function())
print(function())
