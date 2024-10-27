a = {'green': 1, 'blue': 2, 'red': 3}
print(list(map(lambda x: a.get(x), a)))