class Student:
    def __init__(self, id, score):
        self.id = id
        self.score = score


class Score_App:

    students = []

    def __init__(self, file_name):
        self.read_student_data(file_name)

    def read_student_data(self, fn):
        print("file name: {0}".format(fn))
        filename = open(fn, "r")
        for line in filename.readlines():
            split_line = line.split(",")
            object_id = split_line[0]
            object_score = split_line[1]
            new_object = Student(object_id, float(object_score))
            self.students.append(new_object)

    def print_all(self):
        for obj in self.students:
            print(obj.id + ": " + str(obj.score))

    def get_max_score(self):
        maximum = 0
        for obj in self.students:
            if maximum < obj.score:
                maximum = obj.score
        return maximum

    def get_average_score(self):
        total = 0
        count = 0
        for obj in self.students:
            total += obj.score
            count += 1
        return total/count


def count_pass_score(student_list):
    a = 0
    for i in student_list:
        if i.score > 50:
            a += 1
    return a


def get_total_score(student_list):
    total_score = 0.0
    for i in student_list:
        total_score += i.score
    return total_score


app = Score_App("data.txt")

print("-" * 30)
app.print_all()

print("-" * 30)
print("Max score: " + str(app.get_max_score()))
print("Average score: " + str(app.get_average_score()))
print("Number of pass scores: {0}".format(count_pass_score(app.students)))
print("Total score: {0}".format(get_total_score(app.students)))
