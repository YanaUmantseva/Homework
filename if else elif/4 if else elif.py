a = input('Введите букву: ')
vowel = 'аеёяюиоуыэ'

if a in vowel:
    print('гласная')
elif a.isalpha():
    print('согласная')
else:
    print('не буква')


#Напишите программу, которая определяет,
# является ли введенный символ гласной или согласной буквой. a.isalpha(): явл ли буквой