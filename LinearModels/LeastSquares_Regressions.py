# -*- coding: utf-8 -*-
"""
@author: swmapthingpaul (pjulian@ufl.edu)

"""
#Original code from from https://towardsdatascience.com/total-least-squares-in-comparison-with-ols-and-odr-f050ffc1a86a

#clears everything
# %reset

#Libraries
import os
import numpy
import pandas as pd

from numpy.linalg import inv
import statsmodels.api as sm
import numpy.linalg as la
import scipy.odr as odr
import matplotlib.pyplot as plt

## Find working directory
os.getcwd()

# Change working directory
os.chdir('D:\\_GitHub\\learningpython\\LinearModels')

#Sample data (sample_data_tls.py)
# https://gist.github.com/RyotaBannai/a069070dfd5be78d6bb4c8248ef71604
N=60
mu=0
sd=2

numpy.random.seed(0);#similar to set.seed() in r
ran = numpy.random.normal(size=N);#similar to rnorm() in r
error1 = sd**2 * ran + mu
error2 = sd*.5 * ran + mu

lin = numpy.linspace(-15., 15., num=N);#simlar to seq() in r
data = lin + error2
data_true = lin

# Extra combined the data into a data frame simlar to data.frame() in r
dat={'data':data,'data_true':data_true,'x':ran}
dat=pd.DataFrame(data=dat)


##
##
##
# Still figuring this out..
##
##
#ordinary least square model (ols.py)
# https://gist.github.com/RyotaBannai/97aaeb99d2584a349630c9646376502f

x = sm.add_constant(x) # add constant in the 0 index
b = inv(x.T.dot(x)).dot(x.T).dot(y)
yest_ols = numpy.array([b[2]*v**2 + b[1]*v + b[0] for v in x.T[0]])

# with using numpy.linalg.lstsq
b1, b2, c = numpy.linalg.lstsq(sm.add_constant(x).T[[1,2,0]].T, y_data, rcond=None)[0]
yest_ols_ = numpy.array([b2*v**2 + b1*v + c for v in data])

# As a function
def ols_fun(x,y):
    x = sm.add_constant(x) # add constant in the 0 index
    b = inv(x.T.dot(x)).dot(x.T).dot(y)
    yest_ols = numpy.array([b[2]*v**2 + b[1]*v + b[0] for v in x.T[0]])
    return yest_ols
ols_fun(ran,data)