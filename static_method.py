"""Basically the static methods are used to make a function in class without init/cls argument"""

class Student:
    def __init__(self,student_name,student_rollno):
        self.name=student_name
        self.rollno=student_rollno

    def print_details(self):
        return f"The name of the student is {self.name} and the roll no is {self.rollno}"

    #creating a static class
    @staticmethod
    def name_of_school():
        return "Smita Patil Public School."

#creating the instances
student1=Student("Mayur Manohar Patil",4)
student2=Student("Manohar Vasant Patil",77)

print(student1.print_details())
print(student2.print_details())

print(Student.name_of_school())
