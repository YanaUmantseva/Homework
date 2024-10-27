a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = [i for i in range(a, b + 1) if i %2 == 0]
print(c)





#Создать список всех четных чисел от a до b. a и b вводятся с клавиатуры.
#c=0
#for i in range(a, b+1):
#if i % 2 == 0:
#c.append(i)