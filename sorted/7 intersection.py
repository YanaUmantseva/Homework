def intersection(list1, list2):

    return list(set(list1) & set(list2))


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

result = intersection(list1, list2)
print(result)



#Напишите программу, которая принимает на вход два списка и возвращает новый список,
# содержащий элементы, которые есть в обоих списках.