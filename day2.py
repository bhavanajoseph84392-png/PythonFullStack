'''
Operators
---------------------
1.Arithmetic
+,-,*,//,**
print(2*3)
print(4%5==0)
print(10**2)
print(10/2)
print(35.20//5)


----------------------
2.Assignment
++,--,==,+=,-=
count =0
for j in range(1,10):
    count+=1
    print(count)
-----------------------
3.Comparison
==*:looks for both values equal or not
,!=,>=,<=,<,>
a=7
b=9
print(a==b)

4.Logical
------------
and-->This is used to check both should be true
or-->
not-->
a = 15
if a% 3 == 0 and  a % 5 ==0:
    print("True")

a = 15
if a% 3 == 0 or  a % 5 ==0:
    print("True")
-------------------------
5.Memebership
---------------------------
in-->
not in-->
a = 7
b = [1,2,8]
print(a not in b)
6.Identity
----------------------
is,is not
a = [1,2] 
b = [1,2]
c = a
print(a==b)
print(id(a))
print(id(b))
print(id(c))
is--->this operator looks for the object is same or not
is not-->
a = [1,2] 
b = [1,2]
c = a
print(type(a))
print(a==b)
print(id(a))
print(id(b))
print(id(c))
print(a is not b)
7.Bitwise
&,|,<<,>>
0101
0011
-----
0001
print(5|3)
----------------
Data type:
int
float
a = 9 # immutable
b = 7.0
print(a+b)
-------------------
String: It is a sequence of characters that are enclosed in single,double,trile quotes.
single quote- '',
double quotes-""
thriple quotes-''''''
String is immutable data type.
methods:
1.Replace():used to replace with new substring
synatx--> variable_name.replace("old string","new string")
any = "Python is a language "
print(any.replace("Python","Java"))
print(any)

2.Split():used to separate into parts ,and split based on the substring where before substring is one index and after is another index in the list
any =("Python is a language")
print(any.split("$"))
print(any)
syntax--> variable_name.split("substring")

3.len()
-------
-->get number of items,substring
syntax-->len(variable(name))
any = "Python is a language"
print(len(any))

4.Slicing()
-----------
-->can give me access to get particular index from the string.
synatx-->variable_name[starting index : ending index]
print(any[3:11])

5.Indexing()
--------
--->used to get the substring present in that index position...
syntax-->variable_name[index position]
any = "Python is a language"
print(any[7])

6. Index():
any = "Python is a language"
print(any[7])
print(any.index("ang"))

".".join(vari)
count
strip
'''

'''
any = "Python is a language"
print(any[7])
print(any.index("ang"))





