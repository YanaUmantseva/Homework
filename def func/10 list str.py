a = ['green' , 'red' , 'black', 'pink 1', 'apple 4']


def list_str(list1):
    result = []
    for i in list1:
        if i.isdigit():
            result.append(i)
    return result

a = ['green' , 'red' , 'black', 'pink 1', 'apple 4', '345']
print(list_str(a))




#Напишите функцию, которая принимает
# на вход список строк и возвращает список строк, которые содержат только цифры.