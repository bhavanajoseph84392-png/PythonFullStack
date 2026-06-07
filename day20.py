'''
Polymorphism:-
-->This means many forms,it allows same function or operator to behave differently depending on the object......
1.Method overloading
-->Method overloading means defining multiple methods with the same name, but different parameter.
ex:
class calcu_:
    def add(self,a,b,c=0):
        return a + b + c
An = calcu_()
print(An.add(23,6))
print(An.add(23,6,34))
ex:

class calcu_:
    def add(self,a,b,):
        return a + b
    def add(self,a,b,c=0):
        return a+b+c
An = calcu_()
print(An.add(23,6))
print(An.add(23,6,34))

ex:
class calcu_:
    def add(self,*num):
        return sum(num)
    def add(self,*num):
        return sum(num)
An = calcu_()
print(An.add(23,6))
print(An.add(23,6,34))

----------------------
2.Method overriding
-->This occurs when a child provides its own implementation of a method already defined in the parent class....
ex:
class animal:
    def sound(self):
        print("Animal makes sound")
class dog(animal):
    def sound(self):
    
        print("Dog barks")
ntg = dog()
ntg.sound()

class animal:
    def sound(self):
        print("Animal makes sound")
class dog(animal):
    def sound(self):
        super().sound()
    
        print("Dog barks")
ntg = dog()
ntg.sound()
*Note: super()is used to acess methods if that method is present in the parent class.

----------------------
3.Operator Overloading
-->This operator overloading allows such as +,-,* etc to perform different actions to define objects.
ex:
class stu_:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,b):
        return  self.marks+ b.marks
so_1 = stu_(4)
so = stu_(78)
print(so_1+so)

ex:
class stu_:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,other):
        return  self.marks+ other.marks
so_1 = stu_(4)
so = stu_(78)
print(so_1+so)

Note:-
-->The operator inside the method will overload a special method or operator given in the call.
class stu_:
    def __init__(self,marks):
        self.marks = marks
    def __truediv__(self,other):
        return  self.marks/ other.marks
so_1 = stu_(4)
so = stu_(78)
print(so_1/so)


Data Abstraction:-
-->This is the process of hiding internal implementation details and showing only the essential features to the user
-->It focuses on an object rather than how it does it.

from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeters(self):
        pass
class Rec(shape):
    def __init__(self,a,b):
        self.a  = a
        self.b  = b
    def area(self):
        return self.a * self.b
    def perimeters(self):
        return  2*(self.a*self.b)
an = Rec(10,5)
print(an.area())


'''

from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeters(self):
        pass
class Rec(shape):
    def __init__(self,a,b):
        self.a  = a
        self.b  = b
    def area(self):
        return self.a * self.b
    def perimeters(self):
        return  2*(self.a*self.b)
an = Rec(10,5)
print(an.area())











































