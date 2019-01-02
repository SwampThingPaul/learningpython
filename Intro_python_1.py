# -*- coding: utf-8 -*-
"""
@author: swmapthingpaul (pjulian@ufl.edu)

"""
## Python 101
## Find working directory
import os
cwd=os.getcwd()
os.chdir('D:\\_GitHub\\learningpython');# Change working directory

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

#conditional
x==y
x<y
x>y
x!=y

y2=4
x==y2

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
surveys_df.columns
surveys_df.shape

type(surveys_df)
surveys_df.dtypes

pd.unique(surveys_df['species_id'])

#Groups in Pandas
surveys_df['weight'].describe();#summary statistics for 'weight'

surveys_df['weight'].min()
surveys_df['weight'].max()
surveys_df['weight'].mean()
surveys_df['weight'].std()
surveys_df['weight'].count()
surveys_df['weight'].median()
surveys_df['weight'].quantile([0.25,0.50,0.75])

# Group data by sex
grouped_data = surveys_df.groupby('sex')
# Summary statistics for all numeric columns by sex
grouped_data.describe()
# Provide the mean for each numeric column by sex
grouped_data.mean()

#Quick summary counts
# Count the number of samples by species
species_counts = surveys_df.groupby('species_id')['record_id'].count()
print(species_counts)

surveys_df.groupby('species_id')['record_id'].count()['DO']

#Quick plots
# Make sure figures appear inline in Ipython Notebook
%matplotlib inline
# Create a quick bar chart
species_counts.plot(kind='bar',color="blue");

## create data
d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
pd.DataFrame(d)

# Plot stacked data so columns 'one' and 'two' are stacked
my_df = pd.DataFrame(d)

#stacked bar plot
my_df.plot(kind='bar',stacked=True,title="Example of Stacked Bar Plot")
my_df.plot(kind='bar',stacked=True,title="Example of Stacked Bar Plot",colors=["green","blue"])


