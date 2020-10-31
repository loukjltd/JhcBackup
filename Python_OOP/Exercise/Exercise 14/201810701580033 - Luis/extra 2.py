# exercise extra 2
'''
student name: Luis
ID: 201810701580033
class: network182
'''
class Course:

    def __init__(self, title, year):
        self.title = title
        self.year = year

    def show_course(self):
        print("The course is {0} {1}".format(self.title, str(self.year)))


class Course_app:

    course_list = []

    def __init__(self, fn):
        self.get_course_data (fn)

    def get_course_data(self, file_name):

        fn = file_name
        f = open(fn,"r")
        for line in f.readlines():
            split_line = line.split(",")
            t = split_line[0]
            y = int(split_line[1])
            c = Course(t,y)
            b = self.course_list
            b.append(c)



    def show_course_list(self,):
        for i in self.course_list:
            Course.show_course(i)

textFile = ".\my_courses.txt"
app = Course_app(textFile)
app.show_course_list()
