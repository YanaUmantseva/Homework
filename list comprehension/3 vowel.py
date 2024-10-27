array = input('Введите строку: ')
vowels = 'aeiou'

c = []
for i in array:
    if i in vowels:
        c.append(i)
c = ''.join(c)
print(c)









#Создать список строк,
# содержащих только гласные буквы из  строки array. array вводится с клавиатуры.