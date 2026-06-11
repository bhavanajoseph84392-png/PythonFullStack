'''
File Handling:-
--->File handler is an object of file to maintain several functions of file like creating,reading,updating and deleting the file.
The two ways to open the file:-
1.open a file:-
-->open()
2.with open()

name = open('filename','mode')as name
-----
------
name.close
modes
-----
'r'-->is used to reading the file, error if file does not exist......
'a'-->is used to add the text into file , if the file doesnot exist it will create a new file..
'w'-->is used to add the text into file but it will override of all text inside the file. if the file does not exist it will create a new file with that name...
'x'-->used to create the file but it will through the error when we use read method,then we need to use write method.
'r' mode to create.........

method
------
write()
read()
------
-->This method can read entire file chunk by chunk
readline()
-->can only read one line at atime
readlines()
'''
any_=open('demo.txt','r')
print(any_.read())
any_.close()
















































