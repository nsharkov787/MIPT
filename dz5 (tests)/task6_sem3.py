import numpy as np


def f(x, y):
    coeff = (np.mean(x*y)-np.mean(x)*np.mean(y))/ (np.mean(x*x)-np.mean(x)*np.mean(x))
    return coeff
