from collections import defaultdict

def tuple_dict(x):
    res = defaultdict(list)
    for key, value in x:
        res[key].append(value)
    return res

a = [('red', 1), ('green', 3), ('pink', 5)]
print(tuple_dict(a))