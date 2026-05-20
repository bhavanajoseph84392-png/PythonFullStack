'''
F- String:
-----------
It is separated by , and also curly braces

Condition Statements
---------------------
if--->to check the statement is true or not
nested if
elif
ex:
num = 5
if num % 2 == 0:
print("Even")

if-else-->else in the if statement, incase the condition becomes false then it will enter into fall-back(else), it will execute whatever inside it.
ex:
num = int(input("Enter a number :"))
if num %2 !=0:
print(f"{num} is a odd number ")
else:
print(f"{num} is a even number")
-------------------------------------
if- statements: age eligibility
ex:
age_ = int(input("Enter your age:"))
if age_>=18:
print("We are eligible to vote)
else:
print(f"we have to wait for {18-age_}more years")
------------------------------------------------
--Check whether the given year by the user is leap year or not
year_ = 2000
if(year_%4 == 0 and year_%100!= 0) or year_%400 == 0:
print(f"{year_} is a leap year")
else:
print(f"{year_}is not a leap year")
-------------------------------------------------
---Check whether the number is positive or neagtive:
num = -9
if num >=0:
print(f"{num} is a positive number")
else:
print(f"{num} is a negative number")
------------------------------------------------------
--Check whether it the student pass or fail:
marks_ = int(input("Enter your marks:"))
stu_name = input("Enter your name:")
if marks_> = 45:
print(f"{stu_name}your passed")
else:
print(f"{stu_name} your failed")
---------------------------------------
---Check whether it is divisible by 3 and 5
num  = 75
if(num % 3 == 0 and num % 5 == 0:
print(f"{num} is divi by 3 and 5")
else:
print(f"{num} not")
'''
year_ = 2000
if(year_%4 == 0 and year_%100!= 0) or year_%400 == 0:
    print(f"{year_} is a leap year")
else:
    print(f"{year_}is not a leap year")
