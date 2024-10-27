a = [1, 'hello', 3.14]

def list (list1, x):
    result = []
    for i in list1:
       if type(i) == x:
           print(result.append(i))
    return result

a = [1, 'hello', 3.14]
x = float
print(list (a, x))

x = int
print(list (a, x))

x= str
print(list (a, x))


# список [1, hello, 3.14] , значение х , при х = int, должно выввести [1]