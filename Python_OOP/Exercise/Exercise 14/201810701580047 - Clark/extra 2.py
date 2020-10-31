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

        for a in f.readlines():
            x = a.split(',')
            t = x[0]
            y = int(x[1])
            c = [t, y]
            Course_app.course_list.append(c)

    def show_course_list(self):

        for a in Course_app.course_list:
            Course(a[0], a[1]).show_course()


textFile = "my_courses.txt"
app = Course_app(textFile)
app.show_course_list()
