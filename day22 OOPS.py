'''
Error Handling:-
--------------------
try:
-->The try block ,tests a blcok of code for error.
except:
-->The except block let the handle if the code contains errors....
try:
    print(10/0)
except:
    print('This will handle ZeroDivisionError')
-->else block:this will be executed, if the try block has no error in the code.

try:
    print("ANy")
except NameError:
    print('This will handle NameError')
else:
    print("No error")


try:
    print(5+"Py")
except NameError:
    print('This will handle NameError')
else:
    print("No error")

try:
    print(5+"Py")
except AttributeError:
    print('This will handle NameError')
else:
    print("No error")

try:
    prin(5+"P")
except TypeError:
    print('This will handle NameError')
else:
    print("No error")
Note**:
It will only handle the try block code.
try:
    print(5+"Py")
    print(a)
except TypeError:
    print('This will handle TypeError')
except NameError:
    print('This will handle NameError')
else:
    print("No error")

try:
    print("Hi")
except TypeError:
    print('This will handle TypeError')
except NameError:
    print('This will handle NameError')
else:
    print("No error")



Finally block:-
-->This will be exceuted either try block contain error or not...


'''
try:
    print("Hi")
except TypeError:
    print('This will handle TypeError')
except NameError:
    print('This will handle NameError')
else:
    print("No error")










































