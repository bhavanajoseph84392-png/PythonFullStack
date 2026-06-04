'''
OOPS:-
Object oriented Programming and System.
1.Class
-->A class is a blueprint or a template used to create object.
class stu_:
    name = 'Bhavana'
s1= stu_()
print(s1.name)

class stu_:
    def edu_(self):
        print("I am studying B.Tech")
    def sports_(self):
        print("cricket")
        print("Volleyball")
s1 = stu_()
s1.sports_()

2.Object
--> An object is an instance of a class
class stu_:
    name = 'BHAVANA'
s1=stu_()
print(s1.name)
3.
Attributes
-->Attributes are the variables that belongs to a class or a object
4.Methods()
class PFS_DA:
    def python(self):
        PFS_DA = 'Batch_03'
        print('This PFS and DA batch03')
    def Flask(self):
        PFS ='Batch_03'
        print('This PFS batch03')
all_ = PFS_DA()
all_.python()
all_.Flask()
self():Holds the values.


4. Constructor __init__:
A constructor is a special method that is automatically called when an object is created
class ATM:
    def __init__(self,Balance,name):
        self.Balance = Balance
        self.name = name
    def Bal_check(self):
        print(f"{self.name} your total balance is {self.Balance+700}")
    def name_(self):
        print(self.name)
card = ATM(Balance = 50000,name='BHAVANA')
card.Bal_check()
card.name_()

class stu_():
    _name = 'bhavana'
s1 = stu_()
print(s1._stu_name)

5.
Attributes()
1.Public
-->This can be accessed from anywhere in the program
2.Protected()
-->This is represented using a single under score(_).
3.Private()
-->This is represented using a double under score(__)
6. Encapsulation()
-->It is the process of binding data and methods together

'''
class Bank:
    def __init__(self,balance):
        self.__balance = balance
    def depo_(self,amount):
        self.__balance += amount
    def get_bala(self):
        return  self.__balance
acc = Bank(1000)
acc.depo_(10000)
print(acc.get_bala())
