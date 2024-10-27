def sort_students_by_age(students):
    students.sort(key=lambda student: student['возраст'], revers=True )

students_list = [
{'имя': 'Иван', 'возраст': 15, 'оценки': [5, 4, 5]},
{'имя': 'Мария', 'возраст': 14, 'оценки': [4, 5, 3]},
{'имя': 'Сергей', 'возраст': 16, 'оценки': [5, 5, 5]},
{'имя': 'Анна', 'возраст': 13, 'оценки': [4, 4, 4]}]

sort_students_by_age(students_list)
print("Отсортированные ученики по возрасту:", students_list)




#Написать программу , которая принимает список словарей,
# где каждый словарь представляет собой запись об ученике
# (с ключами 'имя', 'возраст', 'оценки'),
# и возвращает список словарей, отсортированный по возрасту учеников
# в порядке убывания.