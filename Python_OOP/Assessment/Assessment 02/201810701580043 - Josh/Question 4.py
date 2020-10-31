#Question 4
#Josh net182 201810701580043

class Book:
    def __init__(self, title, pages):
        self.titile = title
        self.pages = pages

def add_pages(books):
    if len(books) == 0:
        return 0
    else:
        return add_pages(books[1:]) + books[0].pages

books = []
books.append(Book("Learning Python", 673))
books.append(Book("English for Experts", 504))
books.append(Book("OOP in Python", 146))

total_pages = add_pages(books)
print("Total number of pages: {0}".format(total_pages))

