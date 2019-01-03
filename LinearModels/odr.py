import scipy.odr as odr

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