# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:35:42 2020

@author: aradh
"""

"""File Handling:
The key function for working with files in Python is 
the open() function.

The open() function takes two parameters; 
filename, and mode.

There are four different methods (modes) for opening a
 file:

"r" - Read - Default value. Opens a file for
 reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the 
file if it does not exist

"w" - Write - Opens a file for writing, creates
 the file if it does not exist

"x" - Create - Creates the specified file, returns 
an error if the file exists

In addition you can specify if the file should be
 handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

Syntax
To open a file for reading it is enough to 
specify the name of the file:
    """

f =open("C://FILE/file.txt.txt")

"""
The code above is the same as:
    """

f = open("C://FILE/file.txt.txt", "rt")
"""
Because "r" for read, and "t" for text are the 
default values, you do not need to specify them.

Note: Make sure the file exists, or else you will
 get an error."""
 
"""Read Lines:
You can return one line by using the readline() method:

Example:
    
Read one line of the file:"""

f = open("C://FILE/file.txt.txt", "r")
print(f.readline())

"""
By calling readline() two times, you can read the 
two first lines:

Example:
Read two lines of the file:"""

f = open("C://FILE/file.txt.txt", "r")
print(f.readline())
print(f.readline())

"""
By looping through the lines of the file, you can read
 the whole file, line by line:"""

"""Example:
Loop through the file line by line:

"""
f = open("C://FILE/file.txt.txt", "r")
for x in f:
  print(x)
  
  
"""Close Files:
It is a good practice to always close the file when
 you are done with it.

Example:
Close the file when you are finish with it:"""

f = open("C://FILE/file.txt.txt", "r")
print(f.readline())
f.close()


"""Note: You should always close your files,
 in some cases, due to buffering, changes made to a
 file may not show until you close the file."""
 
 
""" Write to an Existing File:
To write to an existing file, you must add a parameter
 to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content

Example:
Open the file "C://FILE/file.txt.txt" and append 
content to the file:
"""
f = open("C://FILE/file.txt.txt", "a")
f.write("Now the file has more content!")
f.close()

"""open and read the file after the appending:"""

f = open("C://FILE/file.txt.txt", "r")
print(f.read())

"""
\Example:
Open the file "C://FILE/file.txt.txt" and overwrite
 the content:
     """

f = open("C://FILE/file.txt.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("C://FILE/file.txt.txt", "r")
print(f.read())

"""
Note: the "w" method will overwrite the entire file.

Create a New File
To create a new file in Python, use the open() 
method, with one of the following parameters:

"x" - Create - will create a file, returns an 
error if the file exist

"a" - Append - will create a file if the 
specified file does not exist

"w" - Write - will create a file if the
 specified file does not exist

Example:
Create a file called "myfile.txt":"""

f = open("myfile.txt", "x")

"""
Result: a new empty file is created!"""

"""Example
Create a new file if it does not exist:"""

f = open("myfile.txt", "w")


 
"""Delete a File:
To delete a file, you must import the OS module, 
and run its os.remove() function:
    

Example:
Remove the file:"""

    
import os
os.remove("C://FILE/file.txt.txt")

"""
Check if File exist:
To avoid getting an error, you might want to 
check if the file exists before you try to delete it:

Example
Check if file exists, then delete it:"""

import os
if os.path.exists("C://FILE/newfile.txt.txt"):
  os.remove("C://FILE/newfile.txt.txt")
else:
  print("The file does not exist")
  
  """
Delete Folder:
To delete an entire folder, use the os.rmdir() method:

Example
Remove the folder "myfolder":
    """

import os
os.rmdir("C://NEWFILE")

"""
Note: You can only remove empty folders."""
 
 
 

