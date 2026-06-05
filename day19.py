'''
Inheritence:
-->This allows the one class to acquire the properties and methods of another class .........
Types:-
1.Single Inheritence
-->A class inherits from a single parent class...
ex:
class father:
    def Land(self):
        print("My father have 5A")
class Jenny(father):
    def my_own(self):
        print('I have 2A')
fam = Jenny()
fam.Land()

PARENT
   |
 CHILD


2.Multiple Inheritence
-->A child class from multiple parents  is called multiple inheritence.
FATHER-MOTHER
 |
CHILD
EX:
class father:
    def Land(self):
        print("My father have 5A")
class Mother:
    def gold(self):
        print("My mother have 1kg G")
class son(father,Mother):
    def mine(self):
        print('I have nothing')
all_= son()
all_.Land()
all_.gold()


3.Multiple -level Inheritence
-->A class inherits from a parent class and another class inherit from that child class .
ex:
class grandfather:
    def land(self):
        print("My grandgather have 5A of land")
class father(grandfather):
    def flat(self):
        print("Have flat at Banglore")
class son(father):
    def Nothing(self):
        print("I have both properties")
all_= son()
all_.land()
all_.flat()
all_.Nothing()

4.Hierarchial Inheritence
-->Multiple chains inherit from a single parent..........
ex:
class father:
    def land(self):
        print("10 acres  of land")
class Jenny(father):
    def mine(self):
        print("Job")
class Jack(father):
    def bro(self):
        print("Jobless")
Ja = Jack()
Ja.land()
so = Jenny()
so.land()
    

5.Hybrid Inheritence
-->This is the combination of two or more types of inheritence
class A:
    def some(self):
        print('Class A')
class B(A):
    def any(self):
        print('Class B')
class C(A):
    def so(self):
        print('Class C')
class D(B,C):
    def All_(self):
        print('Class D')
how =D()
how.so()

6. supermethod()
-->super()is used to access methods and constructor of the parent class from the child class
ex:
class parent:
    def display(self):
        print('Method Parent')
class child(parent):
    def display(self):
        super().display()
        print('Method Child')
any_ = child()
any_.display()

'''
class Person:
    def __init__(self,name):
        self.name = name
class stu_(Person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll
    def show(self):
        print(f"Name:{self.name}")
        print(f"RollNo:{self.roll}")
e =stu_("jarvis",23)
e.show()




















