a = ['green' , 'red' , 'black', 'pink', 'apple']

def list_str(list1):
    result = []
    for i in list1:
        if 'e' in i.lower():
            result.append(i)
    return result

a = ['green' , 'red' , 'black', 'pink', 'apple']
print(list_str(a))



#Напишите функцию, которая принимает
# на вход список строк и возвращает список строк, которые содержат букву "e".