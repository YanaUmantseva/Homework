a = [1, 11, 14, 5, 6, 21]

def list_numbers(num):
    result = []
    for i in num:
        if i > 10 and i < 20:
            result.append(i)
    return result


a = [1, 11, 14, 5, 6, 21]
print(list_numbers(a))

#rang(10, 20)






#Напишите функцию, которая принимает
# на вход список чисел и возвращает список чисел, которые больше 10 и меньше 20.