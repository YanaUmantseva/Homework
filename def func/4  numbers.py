a = [1, 2, 3, 4, 5, 6]

def numbers(num):
    result = []
    for i in num:
        if i % 2 == 0:
            result.append(i)
    return result

a = [1, 2, 3, 4, 5, 6]
print(numbers(a))



#Напишите функцию, которая
# принимает на вход список чисел и возвращает только четные числа из этого списка.