a = 5
b = 5
c = 5

if a <= 0 or b <= 0 or c <= 0:
    print("положительный")
elif a == b == c:
    print('равносторонний')
elif a == b or b == c or a == c:
    print('равнобедренный')
else:
    print('разносторонний')


#Напишите программу, которая определяет,
# является ли треугольник равносторонним, равнобедренным или разносторонним.
#Равнобедренный треугольник — это треугольник, в котором две стороны равны.