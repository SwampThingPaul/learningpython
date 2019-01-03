import numpy as np
from numpy.linalg import inv
import statsmodels.api as sm

# from scratch
x = sm.add_constant(x) # add constant in the 0 index
b = inv(x.T.dot(x)).dot(x.T).dot(y)
yest_ols = np.array([b[2]*v**2 + b[1]*v + b[0] for v in x.T[0]])

# with using numpy.linalg.lstsq
b1, b2, c = np.linalg.lstsq(sm.add_constant(x).T[[1,2,0]].T, y_data, rcond=None)[0]
yest_ols_ = np.array([b2*v**2 + b1*v + c for v in data])