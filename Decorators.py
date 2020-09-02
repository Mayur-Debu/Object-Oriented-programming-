"""Decorator program"""
def dec1(fun):
    def executing():
        a=int(input("ENTER NUMBER: "))
        b=int(input("ENTER NUMBER: "))
        fun(a,b)
    return executing

@dec1                   #decorator
def function_1(a,b):
    print(f"Addition of the both number is: {a+b}")


function_1()            #function call