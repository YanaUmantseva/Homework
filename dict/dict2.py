color1 = {'green': 1, 'blue': 2, 'red': 3}
color2 = {'white': 4, 'black': 5, 'pink': 6}
color3=color1.copy()

color3.update(color2)
print(color3)






#Напишите программу, которая принимает два словаря
# (с ключами типа str и значениями int) и объединяет их.
# Если в обоих словарях есть одинаковые ключи, значения должны быть сложены.
#update обновление одного словоря , добавляя пары ключ с другого словаря