class A:
    def __init__(self):
        # self.instanceVariable1="I am a class A instance variable"
        self.specialVariable="I am a special variable in class A"
class B(A):
    def __init__(self):
        super().__init__()
        self.instanceVariable1="I am a class B instance varibale"

a=A()
b=B()

print(b.specialVariable)       #if super doesn't exist then it's not printed.
print(b.instanceVariable1)     #it searches for class B first if their is instance variable then it prints otherwise it the instance variable present in class B
""" 
Output of line no 14: I am a class B instance varibale
If I disabled the line no: 8 then the output will be:
I am a class A instance varibale"""

