# assessment2 quertion4
'''
student name: felix
#ID: 201810701580052
#class: net182
'''
class Book:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages

def add_pages(books):
    if len(books)==0:
        return 0
    else:
        newbooks=books[1:len(books)]
        return books[0].pages+add_pages(newbooks)


books = []
books.append(Book("Learning Python", 673))
books.append(Book("English for Experts", 504))
books.append(Book("OOP in Python", 146))

total_pages = add_pages(books)
print("Total number of pages: {0}".format(total_pages))