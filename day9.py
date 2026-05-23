'''
1.Nested for loop:-
-->The loop gets completed when it is equal to first for loop 
ex:
for i in range(1,10):
    for j in range(1,2):
        print(j)
logic for tables
ex:
num = 9
for j in range(1,10):
    print(f"{num}x {j} = {j*num}")

2.String Reversing:-
ex:
so = input("Enter a word:")
empty_str = ""
for j in so:
    empty_str = j + empty_str
    print(empty_str)
if empty_str == so:
    print(f"{so} is palindrome")
else:
    print(f"{so} is not a palindrome")
3.Amstrong Number:-
num = 93084
amstro_ =0
length_ = len(str(num))
for i in  str(num):
    amstro_+=int(i)**length_
if amstro_ == num:
    print(f"{num} is a amstrong number")
else:
    print(f"{num} is not a amstrong number")
4.Perfect Number:-
ex:
num = 28
per_num=0
for j in range(1,num):
    if num % j == 0:
        per_num +=j
if per_num == num:
    print(f"{num} is a perfect num")
else:
    print(f"{num} is not a perfect num")

5. Prime Number:-
ex:
num = int(input("Enter anumber:"))
count = 0
for k in range(1,num+1):
 if num % k == 0:
         count+=1
if count == 2:
         print(f"{num} is a prime number")
else:
        print(f"{num} is not a prime number")
6. Patterns:-
star_ = 5
count = 0
for g in range(1,star_+1):
    for d in range(1,g+1):
        count+=1
        print(d, end=" ")
    print()

7.for 5 star patterns:
star_ = 5
count = 0
for g in range(star_,0,-1):
    for d in range(g):
        count+=1
        print("*", end=" ")
    print()
8.pyramid pattern stars:-
ex:
num = 5
for j in range(1,num+1):
    print(" "*(num-j),end="")
    for i in range(1,j+1):
        print("*",end=" ")
    print()
9. pattern for characters:-
ex:


'''
