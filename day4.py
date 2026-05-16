'''
Concatination:
-------------
-->The (+)for int and can add , but for the other data types it will act as concatenainating the data type
a = 90
b = 8
print(a + b)
any_ = "Python"
so = "is a language"
print(any_+ so)
an = [1,2]
am = [3,4]
print(an + am)

2. Tuple:
------>collection of different data types separated by commas,represented in ()and immutable
ex:
some = (1, "Python",[1,2],(3,4),"Python")
print(some.index("Python"))
methods:
count()
-------
-->this is used to count the particular item in the tuple
syntax--> variable_name.count(item)
ex:
some = (1, "Python",[1,2],(3,4),"Python")
print(some.count("Python"))

index()
-------
--> used to find out the index position of the item, and only gives the first occurance
ex:
some = (1, "Python",[1,2],(3,4),"Python")
print(some.index("Python"))
any  = {1,"Python",[1,2,[34, "this is python 3rd class",78],
                    "Python is a language",89],34,[3,4]}
print(any[2],[2],[1],[8])
print(any[2],[4])

Dictionary()
------>It is  key: value pair, key and value separated by : and pair is separated by comma .
--->represented in curly braces{}
ex:
teja_details =  {"Name":  "Teja",
                 1:2 ,
                 (1,2) :[3,4]}
print(type(teja_details))

Values()
----------
---> used to get all the values from the dict
syntax--> dict.values()
ex:
teja_details = {"Name": "Teja",
                "age" : 45,
                "MobN" : "123456789",
                "Pan" : "GPXPB2072H"}
print(teja_details.values())

items()
--------
--->used to get key and value together
syntax-->dict.items()
ex:teja_details = {"Name": "Teja",
                "age" : 45,
                "MobN" : "123456789",
                "Pan" : "GPXPB2072H"}
print(teja_details.items())
teja_details = {"Name": "Teja",
                "age" : 45,
                "MobN" : "123456789",
                "Pan" : "GPXPB2072H"}
print(teja_details.items())
print(teja_details["age"])

update():
--->used to add a key:value pair into dict
syntax--> dict.update({key:value})

'''
teja_details = {"Name": "Teja",
                "age" : 45,
                "MobN" : "123456789",
                "Pan" : "GPXPB2072H"}

teja_details.update({"Adhaar": "1234567890355564"})
print(teja_details)

teja_details = {"Name": "Teja",
                "age" : 45,
                "MobN" : "123456789",
                "Pan" : "GPXPB2072H"}

teja_details["Adhaar"]: "1234567890355564"
teja_details['Name']  : "Garikapati"
print(teja_details)
