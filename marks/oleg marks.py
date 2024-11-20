def max_fives(n, marks):
    max_fives = 0
    actual_fives = 0
    segment_valid = False

    for mark in marks:
        if mark == 2 or mark == 3:

            if segment_valid:
                max_fives = max(max_fives, actual_fives)
                segment_valid = False
            actual_fives = 0
        else:
            if mark == 5:
                actual_fives += 1
                segment_valid = True


    if segment_valid:
        max_fives = max(max_fives, actual_fives)

    return max_fives if max_fives > 0 else -1


n = int(input("Введите количество оценок: "))
marks = list(map(int, input("Введите оценки через пробел: ").split()))

result = max_fives(n, marks)
print(result)