text ='Привет мир'

text1= text.split()
dct = dict()

for word in text1:
    dct[word] = text1.count(word)
print(dct)


#zip() функция
#азбиваем сплит строку на слова. split


#Напишите программу, которая принимает строку text и возвращает словарь,
# где ключами являются слова, а значениями — количество их вхождений в строку.

#for word in text1:
#    if word in dict:
#    dict[word] +=1
#    else:
 #    dict[word] = 1
#print(dict)

#dict = {}