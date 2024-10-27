a = [4, 7, 3, 2  ,1]


def list_numbers( num):
    result = []
    for i in num:
        if i % 2 == 0:
            result.append(i ** 2)
    return sum(result)

a = [1, 2, 3, 4 ,5 ,6]
print(list_numbers(a))



#Напишите функцию, которая принимает
# на вход список чисел и возвращает сумму квадратов четных чисел из этого списка.