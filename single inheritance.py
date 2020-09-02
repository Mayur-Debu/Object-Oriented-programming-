class Student(object):
    def __init__(self,name):
        self.name=name

    def get_marks(self,hindi,english,math,science,social_science):
        self.hindi = int(hindi)
        self.english = int(english)
        self.math = int(math)
        self.science = int(science)
        self.social_science = int(social_science)
        sum=self.hindi+self.english+self.math+self.science+self.social_science
        average=sum/5
        print(f"THE AVERAGE OF THE RESULT IS: {average} ")

class Result(Student):
   pass

student1= Result("mayur")
print(student1.name)
student1.get_marks(80,50,10,50,70)