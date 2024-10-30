
def students_age(students):
    return sorted(students, key=lambda student: student['возраст'], reverse=True)


students = [ {'имя': 'Алексей', 'возраст': 16, 'оценки': [5, 4, 5]},
             {'имя': 'Мария', 'возраст': 17, 'оценки': [4, 5, 5]},
             {'имя': 'Иван', 'возраст': 15, 'оценки': [3, 4, 4]},]


print(students_age(students))