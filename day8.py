'''
1.Elif:-
--> it is used to check more conditions
ex:
stu_marks = 50
if stu_marks>=90:
    print("A+")
elif stu_marks>=80:
    print("A")
elif stu_marks>=70:
    print("B+")
elif stu_marks>=60:
    print("B")
elif stu_marks>=50:
    print("C+")
elif stu_marks>=35:
    print("Pass")
else:
    print("Failed")

Write a program to check the max no among the three numbers
num1 = 100
num2 = 99
num3 = 89
if  num1 >  num2 and num3>num2:
    print(num1)
elif num2 > num3 and num1<num2:
    print(num2)
else:
        print(num3)

2.Nested-if:-
-->Inside if is called nested-if
SBI_bank ={"ATM PIN": "6600"}
pin = input("Enter 4 digit ATM pin: ")
if  len(pin) == 4:
    if pin in SBI_bank['ATM PIN']:
        print("Welcome to SBI")
else:
            print("Invalid pin")
3.For:-
-->For statement: used to iterate sequence
ex:list, strings, tuple. only the mentioned are iterables.
any = "Python"
an = [1,2,3,4]
so = (5,6,7,8,9)
for how in any:# how is known as instance in this program.
    print(how)

4.range()
-- >Intial instance
it is a inbuilt function used to generate numbers in sequencetial manner
synatax-->
range(start,end,step)
ex:
for  i in range(50,100,2):
    print(i)
else:
    print("Code ended here")

5.else in for:once the itterations completed this else will be executed.
break: used to exit from the loop based on the condition
ex:
for  i in range(1,10):
    if i == 5:
        break
    print(i)

continue-->used to skip the current itteration based on the condition
for  i in range(1,10):
    if i == 5:
        continue
    print(i)

pass-- it is a space holderfor  i in range(1,10):
for  i in range(1,10):
    if i == 5:
        pass
    print(i)
'''
i = 1
while i <5:
    print(i)
    i+=1

