# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 08:45:27 2019

@author: Julian_P
"""
## Python 101
## Find working directory
import os
cwd=os.getcwd()
os.chdir('D:\\_python\\DataCarpentry');# Change working directory

# Basic operators
x=4
y=2

print(x + y); # Addition
print(x - y);# Subtraction
print(x * y);# Multiplication
print(x / y);# Returns the quotient
print(x % y);# Returns the remainder
print(abs(x));# Absolute value
print(x ** y);# x to the power y

# material from https://thejacksonlaboratory.github.io/python-ecology-lesson/00-short-introduction-to-Python/
#Lists
numbers=[1,2,3]
numbers[0];#in python index starts with 0 not 1 like in R

#For loop
for num in numbers:
    print(num)

#append lists
numbers.append(4)
print(numbers)

#Tuples (immutable lists) use parentheses
a_tuple=(1,2,3)
a_list=[1,2,3]

# Functions in python
def add_function(a,b):
    result=a+b
    return result
add_function(2,2)


# Starting with Data 
## (https://datacarpentry.org/python-ecology-lesson/02-starting-with-data/index.html)

#Read CSV files
import pandas as pd
pd.read_csv("data/surveys.csv");# Note that pd.read_csv is used because we imported pandas as pd
surveys_df = pd.read_csv("data/surveys.csv")

surveys_df.head()
surveys_df.tail()