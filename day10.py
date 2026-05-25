'''
1. -->Assert :  This is  a debugging statement used to check / test whether a cindition is true
#Assert error
num = 15
assert num < 5
print("True")

age = 9 
assert age >=18,"Age must be greather than or equal to 18"
print("Eligible")

Function()
--->A function is a block of code which only execute when it is called
--->You pass data known as parameters into a functions.
---> To avoid repeated lines in code#

def function_name(parameters):---definition
    --------------------
    --------------------
function_name(arguements)
ex:
num = 9
def even(num):
    if num % 2 == 0:
        print(f"{num} Even")
    else:
        print(f"{num} Odd")
even(num)
even(109)

ways to pass arguements
-------------------------
1.Required arguements:--
-->A function 
ex:
num = 9
def even(num,num_2,num_3):
    if num % 2 == 0:
        print(f"{num} Even")
    else:
        print(f"{num} Odd")

even(109,90,)
ex:num = 9
def even(num,num_2):
    if num % 2 == 0:
        print(f"{num} Even")
    else:
        print(f"{num} Odd")

even(109,90,)

2. Default Arguements():-
-->By default, values is defined at parameters even though it will take from the arguements

3.Keyword  arguements
----------------------------
-->we can send arguements with key=value synatx . By this ,the order of arguements does not matter.
ex:

def even(age,Sal,name):
    print(name)
    print(age)
    print(Sal)
even(name="Garikapati",age=89,Sal=75000)

4.Variable length arguements
--------------------------------
Adding a star(*) before the parameter name in the function, receive a tuple of arguements and can acess items with indexes
ex:
def even(*name):
    print(name[3])
even("Garikapati","Teja", "Chowdary", "Sony")
5. Passing by Value:
-------------------------
ex:
name = "Teja"
def even(any):
    print(any)
even(name)

'''



















    
