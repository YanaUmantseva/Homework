import random

class Quiz:
    def __init__(self):
        self.teams = []
        self.questions = []
        self.result = {}

    def set_teams(self):
        teams_count = int(input('Введите количество команд: '))
        if teams_count <= 1:
            return 'Not correct'
        for i in range(teams_count):
            name = input(f'Название команды {i + 1}: ')
            self.teams.append(name)
            self.result[name] = {"счет": 0, "ответы": []}

    def set_questions(self):
       self.questions = [
            {
                "question": "Что такое переменная в Python?",
                "correct_answer": "B",
                "options": ["A) Специальная функция", "B) Имя, которое ссылается на объект", "C) Какой-либо метод",
                            "D) Команда в языке"]
            },
            {
                "question": "Какой из следующих типов данных не существует в Python?",
                "correct_answer": "C",
                "options": ["A) List", "B) Set", "C) Array", "D) Dictionary"]
            },
            {
                "question": "Какой оператор используется для сравнения двух значений?",
                "correct_answer": "B",
                "options": ["A) =", "B) ==", "C) !=", "D) >"]
            },
            {
                "question": "Как вызывается функция в Python?",
                "correct_answer": "C",
                "options": ["A) function_name[]", "B) function_name{}", "C) function_name()", "D) function_name<>"]
            },
            {
                "question": "Какой из следующих методов используется для добавления элемента в список в Python?",
                "correct_answer": "B",
                "options": ["A) add()", "B) append()", "C) insert()", "D) push()"]
            }
        ]

    def ask_questions(self):
        random.shuffle(self.questions)
        for question in self.questions:
            print("\n" + question["question"])
            if question["options"]:
                print("Варианты ответов:")
                for idx, option in enumerate(question["options"], start=1):
                    print(f"{idx}. {option}")

            for team in self.teams:
                answer = input(f"{team}, ваш ответ: ")
                self.result[team]["ответы"].append(answer)
                if answer.lower() == question["correct_answer"].lower():
                    self.result[team]["счет"] += 1
                    print("Правильный ответ!")
                else:
                    print(f"Неправильный ответ. Правильный ответ: {question['correct_answer']}")

    def show_results(self):
        print("\nРезультаты викторины:")
        for team, data in self.result.items():
            print(f"{team}: {data['score']} баллов, Ответы: {data['answers']}")

quiz = Quiz()
print(quiz.set_teams())
print(quiz.set_questions())
print(quiz.ask_questions())
print(quiz.show_results())

