def palindrome(num):
    return str(num) == str(num)[::-1]


def nearest_palindrome(n):
    num = int(n)


    distance = 0
    while True:

        if palindrome(num + distance):
            return num + distance


        if distance > 0 and palindrome(num - distance):
            return num - distance


        distance += 1


print(nearest_palindrome("11"))
print(nearest_palindrome("188"))
print(nearest_palindrome("194"))





#Написать функцию, принимающую число и возвращающую ближайший к этому числу
# палиндром(то, что одинаково читается в другую сторону)
#11 -> 9
#188 -> 191
#194-> 191