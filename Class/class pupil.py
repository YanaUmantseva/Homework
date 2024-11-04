class Student:
    def __init__ (self, name, last_name, age, marks):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.marks = marks

    def mark(self):
        return sum(self.marks)/ len(self.marks())

    def get(self):
        if self.mark() > 8:
            return self.mark(), 'Good'
        else:
            return 'ok'

s = Student( 'Alex', 'Ivanow', 10, [7,8,9,9] )
print(s.mark)
print(s.get)