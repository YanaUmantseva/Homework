

def numbers (num: int):
    result = []
    for i in str(num):
        result += int(i)**2

    return result


a = 321
print(numbers(a))






# Функция принимает число и возвращает сумму квадратов чисел этого чиcла.
#in: 321
#out: 14