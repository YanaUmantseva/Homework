def max_(a):

    b = list(str(a))

    b.sort(reverse=True)

    c = int(''.join(b))
    return c


a = 37291
result = max_(a)
print(result)




#Есть целое число, например a = 37291.
# Переставьте цифры числа так, чтобы получить макс. возможное значение.
# Для 37291 это будет 97321.
#
#