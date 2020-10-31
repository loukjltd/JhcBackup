'''
class:net182
name:Assass
id:201810710580040
'''
class Student:
    def __init__(self,id,score):
        self.id=id
        self.score=score
class Score_App:
    students = []
    def __init__(self, file_name):
        self.read_student_data(file_name)
    def read_student_data(self, file_name):
        f=open(file_name,'r')
        for i in f.readlines():
            b=i.split(',')
            a=Student(str(b[0]),float(b[1]))
            Score_App.students.append(a)
    def print_all(self):
        for i in Score_App.students:
            print(i.id+': '+str(i.score))
    def get_max_score(self):
        m=0
        for i in Score_App.students:
            if i.score>=m:
                m=i.score
        return m
    def get_average_score(self):
        s=0
        for i in Score_App.students:
            s+=i.score
        return s/len(Score_App.students)

    def count_pass_score(self):
        c=0
        for i in Score_App.students:
            if i.score>=50:
                c+=1
        return c
# Outside all of the classes
def get_total_score(student_list):
    if len(student_list)==0:
        return 0
    else:
        a=student_list[1:len(student_list)]
        return student_list[0].score+get_total_score(a)

app = Score_App("./data.txt") # Use the correct location, for example C:\\Users\\XXXX\\Desktop\\data.txt

print("-"*30)
app.print_all()

print("-"*30)
print("Max score: " + str(app.get_max_score()))
print("Average score: " + str(app.get_average_score()))
print("Number of pass scores: " + str(app.count_pass_score()))
print("Total score: " + str(get_total_score(app.students)))
