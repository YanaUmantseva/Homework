from functools import reduce
a = [1, 5,7, 8, 9, 4]
print(reduce(lambda x , y  : x+y,a))