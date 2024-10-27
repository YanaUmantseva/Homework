def count_duplicate_elements(input_list):

    element_count = {}


    for element in input_list:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1


    duplicate_count = sum(1 for count in element_count.values() if count > 1)

    return duplicate_count



input_list = [1, 2, 2, 2, 3, 4, 5, 5, 5, 5, 5, 5]
result = count_duplicate_elements(input_list)
print("Количество повторяющихся элементов =", result)



#Напишите программу, принимающую список и считает кол-во элементов,
# которые встречаются более 1 раза.
#Например в списке [1, 2, 2, 2, 3, 4, 5, 5, 5, 5, 5, 5]
# количество повторяющихся элементов = 2. (это числа 2 и 5)