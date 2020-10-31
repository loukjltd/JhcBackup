# exercise question 4
'''
student name: Luis
ID: 201810701580033
class: network182
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
