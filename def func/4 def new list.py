a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

def new_list (list1, list2):
    new_list1 = set(list1).intersection(list2)
    return list(new_list1)

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
print(new_list(a, b))




#Напишите функцию, которая принимает на вход два списка
# и возвращает новый список, содержащий элементы, которые есть в обоих списках.