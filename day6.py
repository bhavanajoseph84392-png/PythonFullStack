'''
Type Conversions
------------------
int--> it can be converted into float, string.
ex:
an = 78
us = str(an)
om = float(an)
print(om)
print(type(om))
print(type(us))

str-->it can be used to convert into int if it only contains numbers only.

ex:
an = "90"
Ear = int(an)
print(type(Ear))
ex:
an = "90"
Ear = float(an)
print(type(Ear))

an = "90"
Ear = list(an)
print(Ear)
print(type(Ear))

an = "90"
Ear = list(an)
print(Ear)
print(type(Ear))
con = tuple(an)
print(con)

float-->
ex:
Car = 99.7
print(int(Car))
ex:
Car = 99.7
print(int(Car))
print(type(str(Car)))

3.List:
Any = [6,7] convert with str
print(str(Any))

Any = [6,7]
print(str(Any))convert tuple
print(tuple(Any))

4. Tuple to string , lists:-
ex:
how = (4,5)
print(list(how))

how = (4,5)
print(str(how))

int as a user -input
num = int(input("Enter a number:"))
print(100+num)


str as a user-input
some = input("Write a text:")
print(some)

 tuple as a user -input:-
---------------------------
ex:
any = tuple(map(int,input("Enter numbers:") .split()))
'''
num = eval(input("Enter:"))
print(num)

