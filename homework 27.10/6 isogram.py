a = input("Введите слово"

isogram = len(a) == len(set(a))

if isogram:
    print('слово' ,a, "явл изограммой")
else:
    print('слово' ,a, "не явл изограммой")



#


#Пользователь вводит слово с клавиатуры, необходимо проверить,
# является ли это слово изограммой (то есть не содержит одинаковых символов)
#сравнение длины слова, равно ли длина слова и множества.