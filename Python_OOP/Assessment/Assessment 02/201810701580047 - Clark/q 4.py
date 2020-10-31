class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages


def add_pages(books):
    if len(books) == 0:
        return 0
    else:
        return books[0].pages + add_pages(books[1:])


books = [Book("Learning Python", 673), Book("English for Experts", 504), Book("OOP in Python", 146)]
total_pages = add_pages(books)
print("Total number of pages: {0}".format(total_pages))
