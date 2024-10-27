a = [1, 2, 3, 4, 5, 6]

def numbers( num ):
    list1 =[]
    for i in num:
        list1.append(i**2)
    return list1

a = [1, 2, 3, 4, 5, 6]
list1 = numbers(a)
print(list1)



#return[i**2 for i in num]




#Напишите функцию,
# которая принимает список чисел и возвращает список квадратов этих чисел.