'''
Sets
-----
-->A set is a collection of unique and unordered elements
-->Duplicate values are not allowed
-->Items are not stored in index order
-->Represented in curly braces{}
ex:
any = {1,2,3,4}
print(any)

methods:
1. union ()
-->It will give all the values or elements from two sets together in one set
syntax-->variable_name.union(another var)

2.Intersection()
----------------
--->to get the both the common elements from both the sets
ex:
any = {70,90,80,100}
an ={799,80,1001}
print(any & an)
print(any.intersection(an))
synatx-->variable_name.intersection(another var)

difference ()
--------------
--> to get the different values from the set
syntax-->variable_name.difference(another var)

Symmetric_Difference ():S_D
----------------------

Functions:
1.add()
--------
--> to add new elements into set
syntax-->variable_name.add(element)
ex:
any = {1,2,2,3,4}
any.add(41)
print(any)

2.update()
-----------
-->to add multiple elements into set
syntax-->variable_name.update([elements])
ex:
any = {1,2,2,3,4}
any.update([41,90])
print(any)


'''
any = {1,2,2,3,4}
any.remove(2)
print(any)

