
class Book:
    def __init__(self, title, author, pages, year ):
        self.title = title
        self.author = author
        self.page = pages
        self.year = year

    def __str__ (self):
        return f" {self.title} , {self.author} , {self.page} , {self.year}"

    def set_author(self, new_author):
        self.author= new_author

b = Book('Грокаем алгоритмы', 'Адитья Бхаргава', '288', '2017')
print(b)
