def special_number(a):

    special_list = {'0', '1', '2', '3', '4', '5'}
    for i in str(a):
        if i not in special_list:
            return False
    return True


print(special_number(12))
print(special_number(5))
print(special_number(62))
print(special_number(123450))
print(special_number(1234560))


#Определите является ли число специальным, по определению специальное число - это число, которое состоит только из чисел 0, 1, 2, 3, 4 или 5. Например:
#12 - специальное
#5 - специальное
#62 - нет
#123450 - специальное
#1234560 - нет