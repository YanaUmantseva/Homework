a = ['green' , 'red' , 'black', 'pink', 'apple']

def list_str(list_a):
    result= []
    for i in list_a:
        if i.startswith('a'):
            result.append(i)
    return result

a = ['green' , 'red' , 'black', 'pink', 'apple']
print(list_str(a))






#Напишите функцию, которая принимает
# на вход список строк и возвращает список строк, которые начинаются с буквы "a".