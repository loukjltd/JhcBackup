#Question 6
"""
class:net182
name:vivi
id:201810701580049
"""

class Student:
    def __init__(self, id, score):
        self.id = id
        self.score = score


class Score_App:
    students = []

    def __init__(self, file_name):
        self.read_student_data(file_name)

    def read_student_data(self, file_name):
        f = open('{0}'.format(file_name), 'r')
        try:
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
        max_list = []
        for i in self.students:
           max_list.append(i.score)
        return max(max_list)

    def get_average_score(self):
        score_list = []
        for i in self.students:
            score_list.append(i.score)
        return sum(score_list)/len(score_list)

    def count_pass_score(self):
        count = 0
        for i in self.students:
            if i.score >= 50:
                count +=1
        return count

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
