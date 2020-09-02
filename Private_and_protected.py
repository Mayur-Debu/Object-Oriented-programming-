
class Employee:
    _protected=15    #Naming convention for protected
    __private=10     #naming convention for private
    public=11        #naming convention for public variable

class Employee_inheritance(Employee):
    pass

class Different:
    public = 20
    pass             # THe protected variables can only be accessed by inherited classes not different classes.

employee1=Employee_inheritance()
print(employee1._protected)         #access the protected variable like this
print(employee1._Employee__private) # access the private variables like this

employee2=Different()
# print(employee2._protected)        #will give error
print(employee2.public)              #only has the acess the public private and protected variable of it's own