from abc import ABC, abstractmethod


class Reading:
    def __init__(self, number_of_pages):
        self.number_of_pages = number_of_pages

    @abstractmethod
    def details(self):
        pass


class Book(Reading):
    def __init__(self, number_of_pages, author):
        Reading.__init__(self, number_of_pages)
        self.author = author

    def details(self):
        print("The book was written by %s and has %s pages" % (self.author, self.number_of_pages))


class Newspaper(Reading):
    def __init__(self, number_of_pages, issue_date):
        Reading.__init__(self, number_of_pages)
        self.issue_date = issue_date

    def details(self):
        print("The newspaper is for %s and has %s pages" % (self.issue_date, self.number_of_pages))


readings = [Book(545, "Dan Brown"), Book(675, "Stephen King"), Newspaper(54, "2017/11/01"), Newspaper(34, "2017/10/23")]
total = 0
for i in readings:
    i.details()
    total = total+i.number_of_pages
print("Total number of pages:", total)


