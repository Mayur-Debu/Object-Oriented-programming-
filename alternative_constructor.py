"""Class method as an alternative constructor."""

class Student:
     def __init__(self,student_name,student_rollno,student_std):
         self.name=student_name
         self.rollno=student_rollno
         self.std=student_std

     @classmethod
     def from_str(cls,string):
         attribute=string.split("-")
         return cls(attribute[0],attribute[1],attribute[2])

student1=Student("Mayur",12,8)         #using init
print(student1.rollno)

student2=Student.from_str("MANOHAR-12-10")  #using class method as an alternative contructor
print(student2.name)
