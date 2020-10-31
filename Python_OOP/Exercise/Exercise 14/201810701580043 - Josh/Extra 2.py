#Extra 2
#Josh net182 201810701580043

class Course:

    def __init__(self, title, year):
        self.title = title
        self.year = year

    def show_course(self):
        print("The course is {0} {1}".format(self.title, str(self.year)))


class Course_app:

    course_list = []

    def __init__(self, fn):
        self.get_course_data(fn)

    def get_course_data(self, file_name):
        f = open(file_name, 'r')
        for l in f.read().splitlines():
            line_list = l.split(',')
            t = line_list[0]
            y = int(line_list[1])
            c = Course(t, y)
            self.course_list.append(c)

    def show_course_list(self):
        for c in self.course_list:
            c.show_course()

textFile = './my_courses.txt'
app = Course_app(textFile)
app.show_course_list()
