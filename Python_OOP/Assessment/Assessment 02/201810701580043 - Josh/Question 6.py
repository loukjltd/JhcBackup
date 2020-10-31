#Question 6
#Josh net182 201810701580043

class Student:
    def __init__(self, id, score):
        self.id = id
        self.score = score


class Score_App:
    students = []

    def __init__(self, file_name):
        self.read_student_data(file_name)

    def read_student_data(self, file_name):
        try:
            f = open('./{0}'.format(file_name), 'r')
            for i in f.read().splitlines():
                line_list = i.split(',')
                id = line_list[0]
                score = float(line_list[1])
                self.students.append(Student(id, score))
        except IOError:
            print('Not found')
        finally:
            if f:
                f.close()

    def print_all(self):
        for i in self.students:
            print('{0}:{1}'.format(i.id, i.score))

    def get_max_score(self):
        maxlist = []
        for i in self.students:
           maxlist.append(i.score)
        return max(maxlist)

    def get_average_score(self):
        scorelist = []
        for i in self.students:
            scorelist.append(i.score)
        return sum(scorelist)/len(scorelist)

    def count_pass_score(self):
        count1 = 0
        for i in self.students:
            if i.score >= 50:
                count1 +=1
        return count1

# Outside all of the classes
def get_total_score(student_list):
    if len(student_list) == 0:
        return 0
    else:
        return get_total_score(student_list[1:]) + student_list[0].score


app = Score_App("data.txt")

print("-" * 30)
app.print_all()

print("-" * 30)
print("Max score: " + str(app.get_max_score()))
print("Average score: " + str(app.get_average_score()))
print("Number of pass scores: " + str(app.count_pass_score()))
print("Total score: " + str(get_total_score(app.students)))
