"""if you want to make a function cumpolsory to be implemented by the child class,
then add a abstract class as a parent class.

we cannot make the objects for abstract class...."""

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def printArea(self):
        return self.area*self.breadth

class Rectangle(Shape):
    def __init__(self):
        self.area=7
        self.breadth=6
    def printArea(self):                           # If this line is not included then error are generated as it is a abstract method
        return self.area*self.breadth

object1=Rectangle()
print(object1.printArea())
