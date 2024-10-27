a = [2, 2, 2, 4]

def list_true(list1):
    result = []
    for i in list1:
        if i < 0:
            return False
    return True

a = [2, 2, 2, 4]
print(list_true(a))





#Напишите функцию, которая принимает на вход список чисел и
# возвращает True,
# если все числа в списке положительные, и False в противном случае.