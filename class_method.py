class Student:
    no_of_leaves=8

#constructor
    def __init__(self,name_student,rollno_student,std_student):
        self.name=name_student
        self.rollno=rollno_student
        self.std=std_student

    def print_details(self):
        return f"The name of student is {self.name}, roll no of the student is {self.rollno} and the std in which he studies is {self.std}."

     #it is impossible to change the value of the class variable using the instance variable in order to do that we create a class method.
    @classmethod  #clss method decorater
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves=new_leaves


print(f"No of leaves before changing: {Student.no_of_leaves}")    #before changing
student1=Student("MAYUR MANOHAR PATIL",4,8)

print(student1.print_details())
student1.change_leaves(9)                                         #changed using a class instance
print(f"No of leaves after changing: {Student.no_of_leaves}")     #After changing

#new instances no of leaves will also be changed to 9
student2=Student("MANOHAR VASANT PATIL",24,10)
print(f"NO of Leaves for student 2 is also changed to: {student2.no_of_leaves}")