from collections import Counter

def count_elements(x):
    return Counter(x)



a = [1, 2, 2, 3, 3, 4, 5, 6,7]
print(count_elements(a))