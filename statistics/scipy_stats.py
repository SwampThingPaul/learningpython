# -*- coding: utf-8 -*-
"""
@author: swmapthingpaul (pjulian@ufl.edu)

"""
#Statistics in python
#https://www.scipy-lectures.org/packages/statistics/index.html

#clears everything
# %reset

#Libraries
#Libraries
import os
import pandas as pd
import numpy as np
import scipy
import plotly as py
import matplotlib.pyplot as plt
%matplotlib inline

## Find working directory
os.getcwd()

# Change working directory
os.chdir('D:\\_GitHub\\learningpython\\statistics')

#Data
data=pd.read_csv("d:/_GitHub/learningpython/data/brain_size.csv",sep=";",na_values=".")

#creating from arrays
t=np.linspace(-6,6,20)
sin_t=np.sin(t)
cos_t=np.cos(t)

pd.DataFrame({'t': t, 'sin': sin_t, 'cos': cos_t})

#Manipulating data
data.shape
data.columns
print(data['Gender'])
data[data['Gender'] == 'Female']['VIQ'].mean()

groupby_gender = data.groupby('Gender')
groupby_gender['VIQ'].mean()

# Box plots of different columns for each gender
groupby_gender = data.groupby('Gender')
groupby_gender.boxplot(column=['FSIQ', 'VIQ', 'PIQ'])

# Scatter matrices for different columns
from pandas.tools import plotting
plotting.scatter_matrix(data[['Weight', 'Height', 'MRI_Count']])
plotting.scatter_matrix(data[['PIQ', 'VIQ', 'FSIQ']])


# Hypothesis testing: comparing two groups
from scipy import stats

#1-sample t-test: testing the value of a population mean
stats.ttest_1samp(data['VIQ'], 0)   

#2-sample t-test: testing for difference across populations
stats.ttest_ind(data['FSIQ'], data['PIQ'])
data.boxplot(column=["FSIQ","PIQ"])

stats.ttest_rel(data['FSIQ'], data['PIQ'])   

## This is equivalent to a 1-sample test on the difference:
stats.ttest_1samp(data['FSIQ'] - data['PIQ'], 0) 
test=data['FSIQ'] - data['PIQ']
plt.boxplot(test)


#simple linear regression
x = np.linspace(-5, 5, 20)
np.random.seed(1)
# normal distributed noise
y = -5 + 3*x + 4 * np.random.normal(size=x.shape)
# Create a data frame containing all the relevant variables
data = pd.DataFrame({'x': x, 'y': y})

plt.figure(figsize=(5, 4))
plt.plot(data["x"],data["y"], 'o')

from statsmodels.formula.api import ols
model = ols("y ~ x", data).fit()
print(model.summary()) 

# Peform analysis of variance on fitted linear model
from statsmodels.stats.anova import anova_lm
anova_results = anova_lm(model)
print(anova_results)

# Retrieve the parameter estimates
beta_0, beta_1 = model._results.params
plt.plot(x, x*beta_1 + beta_0)
plt.xlabel('x')
plt.ylabel('y')

#data with linear model depicited run all lines together
plt.plot(data["x"],data["y"], 'o')
plt.plot(x, x*beta_1 + beta_0,color="black")
plt.xlabel('x')
plt.ylabel('y')


## Categorical variables: comparing groups or multiple categories
model = ols("VIQ ~ Gender + 1", data).fit()
print(model.summary())


