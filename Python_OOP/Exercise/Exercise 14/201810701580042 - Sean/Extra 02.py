# Exercise Extra 02
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''


class Course:

    def __init__(self, title, year):
        self.title = title
        self.year = year

    def show_course(self):
        print("The course is {0} {1}".format(self.title, str(self.year)))


def show_course_list():

    for i in Course_app.course_list:
        Course.show_course(i)


class Course_app:

    course_list = []

    def __init__(self, fn):
        self.file_name = open("./my_courses.txt", 'r')
        self.get_course_data(fn)

    def get_course_data(self, file_name):

        for i in self.file_name.readlines():
            line_list = i.split(',')
            t = line_list[0]
            y = int(line_list[1])
            c = Course(t, y)
            Course_app.course_list.append(c)


textFile = "./my_courses.txt"
app = Course_app(textFile)
show_course_list()
