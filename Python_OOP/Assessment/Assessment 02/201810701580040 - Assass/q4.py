'''
class:net182
name:Assass
id:201810710580040
'''
class book:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages
def add_pages(books):
    if len(books)==0:
        return 0
    else:
        a=books[1:len(books)]
        return books[0].pages+add_pages(a)
books = []
books.append(book("Learning Python", 673))
books.append(book("English for Experts", 504))
books.append(book("OOP in Python", 146))

total_pages = add_pages(books)
print("Total number of pages: {0}".format(total_pages))
