s  = [3, 4, 5, 6, 8]

b = [n ** 2 for n in s]
print(b)

c = [i %11 for i in s]
print(c)

a = [i for i in s if i%2 == 0]
print(a)

d = [i for i in s if i%2 == 1]
print(d)

n = [i for i in s if s.index(i) +1 %3!=0]
print(n)



#На входе программа получает список целых, не повторяющихся чисел s.
# Ваша задача - вывести следующие списки по одному в строке:
#- Список, состоящий из квадратов s.
#- Список, состоящий из остатков деления на 11 элементов s.
#- Список, состоящий только из чётных элементов s.
#- Список, состоящий только из элементов s с нечётным количеством цифр.
#- Список, состоящий из элементов s, стоящих на позициях, не кратных 3