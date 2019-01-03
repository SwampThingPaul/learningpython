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