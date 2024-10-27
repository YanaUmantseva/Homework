

a = ['green' , 'red' , 'black', 'pink']

def list_str(list_str1):
    result = []
    for i in list_str1:
        if len(i)>5:
            result.append(i)
    return result



a = ['green' , 'red' , 'black', 'pink', 'hello world']

print( list_str(a))





#Напишите функцию, которая принимает
# на вход список строк и возвращает список строк, длина которых больше 5 символов.