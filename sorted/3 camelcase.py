def to_camel_case(s):
    s = s.replace("-", " ").replace("_", " ")

    return ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(s.split()))


print(to_camel_case("the-stealth-warrior"))  # "theStealthWarrior"
print(to_camel_case("The_Stealth_Warrior"))   # "TheStealthWarrior"
print(to_camel_case("The_Stealth-Warrior"))   # "TheStealthWarrior"


#Написать программу , которая будет конвертировать строку в CamelCase. Например:
#"the-stealth-warrior" -> "theStealthWarrior"
#"The_Stealth_Warrior" -> "TheStealthWarrior"
#"The_Stealth-Warrior" -> "TheStealthWarrior"
# Заменяем дефисы и подчеркивания пробелами
# Преобразуем строку в CamelCase