import numpy as np
from scipy.optimize import curve_fit


import Energies as Models
import Nd136

# add limits for the inertia factors
# these limits correspond to 1<=MOI<=125 \hbar^2MeV^-1
A_MIN = 0.004
A_MAX = 1.0
BOUNDS = ([A_MIN, A_MIN, A_MIN], [A_MAX, A_MAX, A_MAX])


def chi2(exp_data, th_data):
    sum_0 = 0
    for i in range(len(exp_data)):
        e = np.power(exp_data[i]-th_data[i], 2)
        sum_0 += e/exp_data[i]
    chi = 1.0/len(exp_data+1)*sum_0
    print(np.sqrt(chi))
