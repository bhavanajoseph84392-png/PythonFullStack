'''
1. Program to convert 24 th clock into normal clock

time_ = input("enter 24 hours time:")
parts_ = time_.split(":")
hours_ =int(parts_[0])
min_ = int(parts_[1])
print(f"{time_}is converted into {hour_ -12}:{min_} pm")

List
-----
--->List is a collection of different data types
--->[] and separated by ,
list is a mutable
any = [1,"Python",[1,2]]
print(any)

any  = [1,"Python",[1,2,[34, "this is python 3rd class",78],
                    "Python is a language",89],34,[3,4]]
print(any[2][2][1][8])
print(any[2][4])
methods
-------
1.append()
------
-->this method is used to add a new item into the list, and it will in the last index position
syntax-->variable_name.append(item)
any = [1,2,3]
any.append(6)
print(any)
any.append([20,90])
print(any)
2.extend():
this is the method is used to add itterable into list , and into list,and it will in the last index position,each value or substring is each index in the list.
syntax:
variable_name.extend(any)
any = [1,2,3,4]
any.extend("Python")
any.extend("python")
print(any)
Immutable
------
-->Could not able to modify on that particular variable
ex: string,integer

Mutable:
-->Can able to modify directly on the variable
ex:list
3.POP():
----
It is useed to remove the item from the list , but will mention here index position in the pop method
syntax:variable_name.pop(index position)
ex:
any = [1,2,3]
print(any.pop(0))
any =[1,2,3]
print(any.pop(4))

4. Remove()
------
It is used to remove the item from the list , but will mention here direct in the remove method
synatx:variable_name.remove(
ex:
any = [1,2,3]
any.remove(2)

'''
so = ["Python",90,"Java"]
so.remove("Python")
print(so)
