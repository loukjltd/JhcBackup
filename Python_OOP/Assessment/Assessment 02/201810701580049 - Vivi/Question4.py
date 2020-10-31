#Question 4
"""
class:net182
name:vivi
id:201810701580049
"""
class Book:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages

sums = 0
def add_pages(books):
    total = 0
    for i in range(len(books)):
        total += books[i].pages
    return total

books = []
books.append(Book("Learning Python", 673))
books.append(Book("English for Experts", 504))
books.append(Book("OOP in Python", 146))

total_pages = add_pages(books)
print("Total number of pages: {0}".format(total_pages))
exit(0)

