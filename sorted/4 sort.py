def sort_k_n(numbers):

    k = [a for a in numbers if a % 2 != 0]
    n = [b for b in numbers if b % 2 == 0]

    return k + n


c = sort_k_n([5, 8, 6, 3, 4])
print(c)







#Программа принимает список чисел и сортирует четные от нечентых:
#[5, 8, 6, 3, 4]  =>  [5, 3, 8, 6, 4] return обьеденяем