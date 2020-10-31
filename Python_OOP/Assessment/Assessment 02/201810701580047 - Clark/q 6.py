class Student:
    def __init__(self, id, score):
        self.id = id
        self.score = score


class Score_App:
    students = []

    def __init__(self, file_name):
        self.read_student_data(file_name)

    def read_student_data(self, file_name):
        f = open(file_name, 'r')
        Score_App.students = []
        for a in f.readlines():
            Score_App.students.append(a.strip('\n').split(','))

    def print_all(self):
        for a in Score_App.students:
            print('%s: %s' % (a[0], a[1]))

    def get_max_score(self):
        x = 0
        for a in Score_App.students:
            if x < float(a[1]):
                x = float(a[1])
        return x

    def get_average_score(self):
        x = 0
        for a in Score_App.students:
            x += float(a[1])
        return x/len(Score_App.students)

    def count_pass_score(self):
        n = 0
        for a in self.students:
            if float(a[1]) >= 50:
                n += 1
        return n


# Outside all of the classes
def get_total_score(student_list):
    x = 0
    for a in student_list:
        x += float(a[1])
    return x


app = Score_App("data.txt")  # Use the correct location, for example C:\\Users\\XXXX\\Desktop\\data.txt

print("-" * 30)
app.print_all()

print("-" * 30)
print("Max score: " + str(app.get_max_score()))
print("Average score: " + str(app.get_average_score()))
print("Number of pass scores: " + str(app.count_pass_score()))
print("Total score: " + str(get_total_score(app.students)))
