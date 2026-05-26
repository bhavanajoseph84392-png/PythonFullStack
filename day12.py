'''
Built-in functions:
--------------------------
print()
input()
len()
type()
max()
min()
ex:
m = [3,4,1,2]
print(sorted(m)): it will sort for only a particular line.
print(m)

m = [3,4,1,2]
m.sort()
print(m)
def fac(num):
    if num == 1:
        return 1
    return num *fac(num-1)

print(fac(5))

def star():
    count = 0
    for x in range(1,star+1):
        if x == 2:
            continue
    for a in range(1,x+1):
        count+=1
        print(a,end =" ")
    print(star(10))
    
def even(num):
    if num % 2 ==0:
        print("Even")
    else:
        print("Odd")
even(16)

def prime(num):
    if num % 5 ==0:
        print("Prime")
    else:
        print("Not Prime")
prime(37)



1. Recursive functions
-------------------------
--->A recursive function that calls itself to solve a problem by breaking it into small or simple sub problems.
2. Return()
-------------
this ends a function and sends a value back to the code that called the function.
ex:
def add(a,b):
    return a+b
res = add(4,5)
print(res)

3.Lambda function:-
single line expression,  annonymous function.
---> a small annonymous fucntion
it will take n type of arguements but single expression
lambda can take n number of arguements but only one expression
ex:
so = lambda a,b,c: a*b*c*a
print(so(3,4,9))

so = lambda a,b,c: a+b+c+a
print(so(3,4,9))

so = lambda a,b,c: a/b/c+a
print(so(3,4,9))

so = lambda a,b,c: a%b/c+a
print(so(3,4,9))
so = lambda a,b,c: a%b/c+a
print(so(3,4,9))
'''
def star(size):
    count = 0
    for x in range(1,s+1):
        if x == 2:
            continue
        for a in range(1,x+1):
            count+=1
            print(a,end =" ")
            print()
s=int(input())
print(star1(s))





























