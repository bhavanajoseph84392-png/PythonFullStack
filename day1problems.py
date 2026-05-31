
def area(A,B):
    A = 20
    B = 30
area = A*B
    print(area)
print()
'''                                        #-----------------------------23/05/2026-------------------------------------------------
1#Write a Python program to calculate the area of a rectangle given its length and width
l = 67
w = 78
area = l*w
print(area)

2#Write a Python program to check if a number is even or odd
num = int(input("Enter a number"))
if(num % 2 == 0):
    print(f"The{num }is even ")
else:
    print(f"The{num } is odd")

 
    ---------------------------------------------------------24/05/2026-----------------------------------------------------------------------------
1. #Create a program that takes a user's name and age as input and prints a greeting message.
user_name = input("Enter the name of the user:")
age       = int(input("Enter the age of the user:"))
print("WELCOME!")
2.
numbers =[34,78,99,200,100]
maximum = numbers[0]
minimum = numbers[0]
for i in numbers:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i
print(f"Maximum value is: {maximum}")

print(f"Minimum value is: {minimum}")
--------------------------------------------------------------25/05/2026--------------------------------------------------------------------------------------------------------------------------
1.
a = 99
b = a
print(b)
2.
num =[56,78,90,-8,500,67]
sum = 0
for i in num:
    if i > 0:
        sum+=i
print(f" Sum of the positive integers is:{sum}")
-----------------------------------------------------------------26/05/2026---------------------------------------------------------------------------------------------------------------------

1.
c = input("Enter a Sentence:")
words = c.split()
count = 0
for i in words:
    count+=1
print(count)

2.
def palindrome(text):
    reverse = text[::-1]
    if text == reverse:
        print(f"{text} is a palindrome")
    else:
        print(f"{text} is not a palindrome")
word = input("Enter a string:")
palindrome(word)
'''
----------------------------------------------------------27/05/2026--------------------------------------------------------------------------------------------------------------------
'''
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))
amount = principal * ((1 + rate / 100) ** time)
compound_interest = amount - principal
print("Compound Interest is:", compound_interest)
print("Total Amount is:", amount)

days = int(input("Enter number of days: "))
years = days // 365
remaining_days = days % 365
weeks = remaining_days // 7
days_left = remaining_days % 7
print("Years:", years)
print("Weeks:", weeks)
print("Days:", days_left)
'''
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def (area):
    A = 20
    B = 30
    print(area)
print()















