class Student:
    no_of_leaves=8

#instance/object
student_1=Student()
student_2=Student()

#Instance variable
student_1.name="Mayur Manohar Patil"
student_1.rollno=4
student_1.std=6

student_2.name="Manohar Vasant Patil"
student_2.rollno=61
student_2.std=8

#class variable
print(Student.no_of_leaves)
print(student_1.no_of_leaves)
print(student_2.no_of_leaves,"\n")

#changing instance variable
student_1.no_of_leaves=5
student_2.no_of_leaves=6

print(Student.no_of_leaves)
print(student_1.no_of_leaves)
print(student_2.no_of_leaves)

#__dict__ returns a dictonary with the attributes of the class/instance whatever requested for....
print(Student.__dict__)
print(student_1.__dict__)
print(student_2.__dict__)

