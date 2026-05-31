'''
def print_pattern(size):
    count = 0

    print("--- Star Triangle ---")
    for i in range(1, size + 1):
        for j in range(1, i + 1):
            count += 1
            print('*', end=" ")
        print()

    print("--- Number Pyramid ---")
    for x in range(1, size + 1):
        for a in range(1, x + 1):
            count += 1
            print(a, end=" ")
        print()

    print("Total items printed:", count)

s = int(input())
print_pattern(s)

def even(num):
    if num % 2 ==0:
        print("Even")
    else:
        print("Odd")
even(16)
def grade(stu_marks):
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
marks = int(input("Enter marks:"))
grade(marks)

def largest(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print("Largest:", num1)
    elif num2 > num1 and num2 > num3:
        print("Largest:", num2)
    else:
        print("Largest:", num3)

num1, num2, num3 = map(int, input("Enter 3 numbers separated by comma: ").split(','))
largest(num1, num2, num3)


def check_number(num):
    if num > 0:
        print(f"{num} is a positive number")
    elif num < 0:
        print(f"{num} is a negative number")
    else:
        print(f"{num} is zero")

num = int(input("Enter number: "))
check_number(num)

def check_leap(year):

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:

        print(f"{year} is a leap year")

    else:

        print(f"{year} is not a leap year")
year = int(input("Enter a year:"))
check_leap(year)

def check_age(vote):

    if vote >= 18:

        print("We are eligible to vote")

    else:

        print(f"We have to wait for {18 - vote} more years")
age = int(input("Enter age:"))
check_age(age)

def result(marks_, stu_name):

    if marks_ >= 45:

        print(f"{stu_name} you passed")

    else:

        print(f"{stu_name} you failed")


marks_ = int(input("Enter your marks: "))

stu_name = input("Enter your name: ")

result(marks_, stu_name)

def check_divisible(num):

    if (num % 3 == 0 and num % 5 == 0):

        print(f"{num} is divisible by 3 and 5")

    else:

        print(f"{num} is not divisible by 3 and 5")
num = int(input("Enter number: "))
check_divisible(num)

def traffic(signal):

    if signal == 1:

        print("Go")

    else:

        print("Stop")


signal = int(input("Enter\n1.Green\n2.Red\n"))

traffic(signal)

def check_armstrong(num):

    temp = num
    sum = 0

    while num > 0:

        digit = num % 10

        sum = sum + (digit ** 3)

        num = num // 10

    if temp == sum:

        print(f"{temp} is an Armstrong number")

    else:

        print(f"{temp} is not an Armstrong number")
num =int(input("Enter a number:"))
check_armstrong(num)

def check_palindrome(num):

    temp = num
    reverse = 0

    while num > 0:

        digit = num % 10

        reverse = reverse * 10 + digit

        num = num // 10

    if temp == reverse:

        print(f"{temp} is a palindrome number")

    else:

        print(f"{temp} is not a palindrome number")
num = int(input("Enter a number:"))
check_palindrome(num)

'''

def atm(pin):

    SBI_bank = {"ATM PIN": "7700"}

    if len(pin) == 4:

        if pin == SBI_bank['ATM PIN']:

            print("Welcome to SBI")

        else:

            print("Incorrect PIN")

pin = input("Enter 4 digit ATM pin: ")

atm(pin)














