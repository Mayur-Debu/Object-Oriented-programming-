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

class Result:
   def __init__(self,marks1,marks2):
       self.marks1=marks1
       self.marks2 = marks2

   def print_info(self):
        print(self.marks1)
        print(self.marks2)

class Print(Student,Result):
    pass

student1=Print("MAYUr")
print(student1.name)