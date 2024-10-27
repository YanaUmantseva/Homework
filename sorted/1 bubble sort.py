def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for c in range(0, n-i-1):
            if array[c] > array[c+1]:
                array[c], array[c+1] = array[c+1], array[c]
    return array

a = [5, 4, 12, 11, 90, 45, 8]
b = bubble_sort(a)
print(b)



#Есть неотсортированный список целых чисел.
# Отсортируйте список по возрастанию,
# не используя встроенные функции sorted(), sort() и т.п.

#bubble sort алгоритм сортировки, последовательно проходит по списку
# и сравнивает соседние элементы меняя их местами 1. получить длину ,