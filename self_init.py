class Student:
    no_of_leaves=8

#constructor
    def __init__(self,name_student,rollno_student,std_student):
        self.name=name_student
        self.rollno=rollno_student
        self.std=std_student

    def print_details(self):
        return f"The name of student is {self.name}, roll no of the student is {self.rollno} and the std in which he studies is {self.std}."


student1=Student("MAYUR MANOHAR PATIL",4,8)  #constructor
print(student1.print_details())
print(student1.no_of_leaves)  #no changes here in the class variable
