# -*- coding: utf-8 -*-
"""
@author: swmapthingpaul (pjulian@ufl.edu)

"""
#Original code from from https://towardsdatascience.com/total-least-squares-in-comparison-with-ols-and-odr-f050ffc1a86a

#clears everything
# %reset

#Libraries
import os
import numpy as np
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

np.random.seed(0)
ran = np.random.normal(size=N)
error1 = sd**2 * ran + mu
error2 = sd*.5 * ran + mu

lin = np.linspace(-15., 15., num=N)
data = lin + error2
data_true = lin

true_func = lambda x, e: .1*x + .1*x**2 + e
x = np.vstack((data, data**2)).T
y_true = np.array([true_func(d, 0) for d in data_true])
y_data = np.array([true_func(d, e) for d,e in zip(data, error1)])


##
##
##
# Still figuring this out..
##
##
#ordinary least square model (ols.py)
# https://gist.github.com/RyotaBannai/97aaeb99d2584a349630c9646376502f
# from scratch
x = sm.add_constant(x) # add constant in the 0 index
b = inv(x.T.dot(x)).dot(x.T).dot(y_true)
yest_ols = np.array([b[2]*v**2 + b[1]*v + b[0] for v in x.T[0]])

# with using numpy.linalg.lstsq
b1, b2, c = np.linalg.lstsq(sm.add_constant(x).T[[1,2,0]].T, y_data, rcond=None)[0]
yest_ols_ = np.array([b2*v**2 + b1*v + c for v in data])

# with using np.linalg.lstsq
b1, b2, c = np.linalg.lstsq(sm.add_constant(x).T[[1,2,0]].T, y_data, rcond=None)[0]
yest_ols_ = np.array([b2*v**2 + b1*v + c for v in data])

#total least square models (tls.py)
# https://gist.github.com/RyotaBannai/db4d26f7c3c3029e320ae1d28864b36c
def tls(X,y):
    
    if X.ndim is 1: 
        n = 1 # the number of variable of X
        X = X.reshape(len(X),1)
    else:
        n = np.array(X).shape[1] 
    
    Z = np.vstack((X.T,y)).T
    U, s, Vt = la.svd(Z, full_matrices=True)
    
    V = Vt.T
    Vxy = V[:n,n:]
    Vyy = V[n:,n:]
    a_tls = - Vxy  / Vyy # total least squares soln
    
    Xtyt = - Z.dot(V[:,n:]).dot(V[:,n:].T)
    Xt = Xtyt[:,:n] # X error
    y_tls = (X+Xt).dot(a_tls)
    fro_norm = la.norm(Xtyt, 'fro')
    
    return y_tls, X+Xt, a_tls, fro_norm

#orthogonal distance regression (odr.py)
# https://gist.github.com/RyotaBannai/e266b81b1750d7c3d2a127fd380986ea

def odr_line(B, x):
    y = B[0]*x + B[1]*x**2
    return y

def perform_odr(x, y, xerr, yerr):
    quadr = odr.Model(odr_line)
    mydata = odr.Data(x, y, wd=1./xerr, we=1./yerr)
    #mydata = odr.Data(x, y)
    myodr = odr.ODR(mydata, quadr, beta0=[0., 0.])
    output = myodr.run()
    return output

regression = perform_odr(data, y_data, np.abs(error2), np.abs(error1))

yest_odr = odr_line(regression.beta, data)


##