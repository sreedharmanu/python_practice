#x="sreedhar"
#y="kumar"
#print(str.upper(x)+" "+y+" is a good boy")

#x="sreedhar"
#y="kumar"
#print(x+" "+ str.upper(y)+" is a good boy")

#x="sreedhar"
#y="kumar"
#print(str.upper(x)+" "+y+" is a good boy")
#print(str.capitalize(),"lower(y)"+" "+y+" is a good boy")

#x="sreedhar"
#y="kumar"
#print(x[0:3]+x[3].upper()+x[4:8]+" "+y+" is a good boy")
#print(x[0].upper()+x[1:8]+" "+y[0].upper()+y[1:5]+" is a good boy")


#x="sreedhar kumar is a good boy"
#print(str .capitalize(x))
#print(str .title(x))

# importing the random module
#import random

#print(random.randint(10000,99999))
#print(random.randrange(1,10000))
#print(random.random())

#x =input("Enter a string: ")
#if num > 5:
 #  print("Positive number")
#elif num == 0:
 #  print("Zero")
#else:
 #  print("Negative number")

#Using set()

#x = ["Mango","Apl", "Mango","grape","bannana"]

#print(x.sort())

#cars = ['FORD', 'BMW', 'Volvo','FORD']
#cars.sort()
#y=cars.sorted(set(cars))
#print(cars)
#print(y)

# Program to sort alphabetically the words form a string provided by the user

#my_str = "Hello this Is an Example With cased letters"

# To take input from the user
#my_str = input("Enter a string")

# breakdown the string into a list of words
#words = [word.lower() for word in my_str.split()]

# sort the list
#words.sort()

# display the sorted words

#print("The sorted words are:")
#for word in words:
#   print(word)

#x="python is a great coding language"
#x=['python', 'grate', 'courses']
#x.sort()
#print(x)

#cars = ['Ford', 'BMW', 'Volvo']

#cars.sort()

#my_str="python is a great coding language"
#my_str= input("Enter a string: ")

#words = [word.lower() for word in my_str.split()]
#words.sort()

#print("The sorted words are:")
#for word in words:
#   print(word)
#for y in x:
#   print(word)
#print( "x in word")
#print("The sorted words are:")
#for x in word:
#   print(y)


#my_str="python,is,a,Great.coding.Language"
#words = [word.upper() for word in my_str.split('.')]
#words.sort()
#for word in words:
#   print(word)


import pathlib

# path of the given file
#print(pathlib.Path("123.txt").parent.absolute())

# current working directory
#print(pathlib.Path().absolute())


import os
#print(' The current working directory is: ', os.getcwd())
#print( __file__)
#print()
#os.getcwd()


int(input('Name : '))
#input()
#print()
#string('Name')