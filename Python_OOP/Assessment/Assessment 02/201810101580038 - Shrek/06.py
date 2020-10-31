# Qusetion 6
'''
Student Name: shrek
ID: 201810101580038
Class: Network 182
'''
class Student:

    def __init__(self, ID, score):
        self.ID = ID
        self.score = score

class Score_App:

    students = []

    def __init__(self, file_name):
        self.read_student_data(file_name)

    def read_student_data(self, file_name):
        self.file_name = open(file_name, 'r')
        for i in self.file_name.readlines():
            split_line = i.split(',')
            student_ID = split_line[0]
            student_score = split_line[1]
            new_student = Student(student_ID, float(student_score))
            Score_App.students.append(new_student)

    def print_all(self):

        for i in self.students:
            print(i.ID+': '+str(i.score))

    def get_max_score(self):
        max_score =0
        for i in self.students:
            if i.score > float(max_score):
                max_score = i.score
        return max_score

    def get_average_score(self):
        tatal=float(0)
        for i in self.students:
            if len(self.students)==0:
                return 0
            else:
                tatal+=i.score
        return tatal/len(self.students)

    def count_pass_score(self):
        b=0
        for i in self.students:
            if i.score>=50:
                b+=1
        return b

def get_total_score(student_list):

    total_score=0
    if len(student_list)==0:
        return 0
    else:
        total_score=student_list[0].score+get_total_score(student_list[1:len(student_list)])
        return total_score


app = Score_App("data.txt") # Use the correct location, for example C:\\Users\\XXXX\\Desktop\\data.txt

print("-"*30)
app.print_all()

print("-"*30)
print("Max score: " + str(app.get_max_score()))
print("Average score: " + str(app.get_average_score()))
print("Number of pass scores: " + str(app.count_pass_score()))
print("Total score: " + str(get_total_score(app.students)))