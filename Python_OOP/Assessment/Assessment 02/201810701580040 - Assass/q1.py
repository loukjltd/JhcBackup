'''
class:net182
name:Assass
id:201810710580040
'''
class worker:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def work(self):
        print('I work')
class teacher(worker):
    def __init__(self,name,age,nos):
        worker.__init__(self,name,age)
        self.nos=nos
    def work(self):
        print('I teach '+ str(self.nos) +' students')
class programmer(worker):
    def __init__(self,name,age,language):
        worker.__init__(self,name,age)
        self.language=language
    def work(self):
        print('I write '+ self.language +' programs')
worker_list = [worker("Sam", 23), teacher("Ted", 33, 27), programmer("Pete", 25, "Python")]
def print_workers(workers):
    for i in workers:
        print(i.name)
        print(i.age)
        i.work()
print_workers(worker_list)
