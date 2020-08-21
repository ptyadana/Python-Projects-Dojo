# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects


class Book:
    def __init__(self, title, price, author):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def getbookpagecount(self):
        total_pages = 0
        for ch in self.chapters:
            total_pages += ch.pages
        return total_pages


class Author():
    def __init__(self, authorfname, authorlname):
        self.authorfname = authorfname
        self.authorlname = authorlname

    def __str__(self):
        return f"{self.authorfname} {self.authorlname}"


class Chapter():
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

    

author = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 39.0, author)

ch1 = Chapter("Chapter 1", 125)
ch2 = Chapter("Chapter 2", 97)
ch3 = Chapter("Chapter 3", 143)
b1.addchapter(ch1)
b1.addchapter(ch2)
b1.addchapter(ch3)

print(b1.title)
print(b1.author)
print(b1.getbookpagecount())
