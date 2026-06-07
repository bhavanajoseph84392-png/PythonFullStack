
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

                                                          28/05/2026


def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]



def reverse_string(s):
    return s[::-1]



def concatenate_names(names):
    return " ".join(names)

def is_pangram(s):
    s = s.lower()
    return all(letter in s for letter in string.ascii_lowercase)


                                                             29/05/2026
def circle_properties(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return round(area, 4), round(circumference, 4)


def convert_minutes(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return hours, minutes
                                                          30/05/2026


def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
                                                        31/05/2026


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]



def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
                                                      1/06/2026


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def names_starting_with_a(names):
    return [name for name in names if name.strip().upper().startswith('A')]



def multiplication_table(n, up_to=10):
    table = []
    for i in range(1, up_to + 1):
        table.append((i, n * i))
    return table



def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def primes_up_to_50():
    return [n for n in range(1, 51) if is_prime(n)]


def count_long_words(words):
    return sum(1 for word in words if len(word) > 5)




