# -*- coding: utf-8 -*-
"""
@author: swmapthingpaul (pjulian@ufl.edu)

"""
## Python 102
#clears everything
# %reset

# https://thejacksonlaboratory.github.io/python-ecology-lesson/02-index-slice-subset/
#Libraries
import os
import pandas as pd

## Find working directory
cwd=os.getcwd()
os.chdir('D:\\_GitHub\\learningpython');# Change working directory

#Read data
surveys_df = pd.read_csv("data/surveys.csv")
#surveys_df2 = pd.read_csv("https://ndownloader.figshare.com/files/2292172");#if you want to direct download into python

# Selecting Data Using Labels (Column Headings)
surveys_df['species_id']
# or 
surveys_df.species_id

# create an object named surveys_species that only contains the `species_id` column
surveys_species = surveys_df['species_id']
# select the species and plot columns from the DataFrame
surveys_df[['species_id', 'plot_id']]
# what happens when you flip the order?
surveys_df[['plot_id', 'species_id']]
#what happens if you ask for a column that doesn't exist?
surveys_df['speciess']


# Create a list of numbers:
a = [1,2,3,4,5]
# select rows 0,1,2 (but not 3)
surveys_df[0:3]

# select the first, second and third rows from the surveys variable
surveys_df[0:3]
# select the first 5 rows (rows 0,1,2,3,4)
surveys_df[:5]
# select the last element in the list
surveys_df[-1:]

# copy the surveys dataframe so we don't modify the original DataFrame
surveys_copy = surveys_df

# set the first three rows of data in the DataFrame to 0
surveys_copy[0:3] = 0
surveys_copy.head()
surveys_df.head()


# Reference versus copying
surveys_df = pd.read_csv("https://ndownloader.figshare.com/files/2292172")
surveys_copy= surveys_df.copy()

#from https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
# Rows:
surveys_df.iloc[0] # first row of data frame
surveys_df.iloc[1] # second row of data frame
surveys_df.iloc[-1] # last row of data frame
# Columns:
surveys_df.iloc[:,0] # first column of data frame 
surveys_df.iloc[:,1] # second column of data frame 
surveys_df.iloc[:,-1] # last column of data frame 

# Multiple row and column selections using iloc and DataFrame
surveys_df.iloc[0:5] # first five rows of dataframe
surveys_df.iloc[:, 0:2] # first two columns of data frame with all rows
surveys_df.iloc[[0,3,6,24], [0,5,6]] # 1st, 4th, 7th, 25th row + 1st 6th 7th columns.
surveys_df.iloc[0:5, 5:8] # first 5 rows and 5th, 6th, 7th columns of data frame


# select all columns for rows of index values 0 and 10
surveys_df.loc[[0, 10], :]

surveys_df.loc[0, ['species_id', 'plot_id', 'weight']]

surveys_df.loc[[0, 10, 35549], :]

surveys_df.iloc[2,6]

# Subsetting using criteria
surveys_df[surveys_df.year == 2002]
surveys_df[surveys_df.year != 2002]
surveys_df[(surveys_df.year >= 1980) & (surveys_df.year <= 1985)]
