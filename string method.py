# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 19:48:06 2021

@author: Raj Patel
"""

#Use the len method to print the length of the string.
x = "Hello World"
print(len(x))

#Get the first character of the string txt.
txt = "Hello World"
x = txt[0]
print(x)

#Get the characters from index 2 to index 4 (llo).
txt = "Hello World"
x = txt[2:5]
print(x)

#Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
x = print(x)

#Convert the value of txt to upper case.
txt = "Hello World" 
txt.upper()
print(txt)

#Convert the value of txt to lower case.
txt = "Hello World"
txt = txt.lower()
print(txt)

#Replace the character H with a J.
txt = "Hello World"
txt = txt.replace("H", "J")
print(txt)

#Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))