a = [5, 8, 6, 3, 4]


def list_numbers(list1):
    even=[]
    odd=[]

    for i in list1:
        if i % 2 == 0:
            even.append(i)
        if i % 2 != 0:
            odd.append(i)
    return odd + even

a = [5, 8, 6, 3, 4]
print(list_numbers(a))



#Функция принимает список чисел и сортирует четные от нечентых:
#[5, 8, 6, 3, 4]  =>  [5, 3, 8, 6, 4]