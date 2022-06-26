from re import M
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
    # print(np.sqrt(chi))
    return np.sqrt(chi)


def do_fit(x_data, y_data, guess):
    exp_data = y_data
    fit_parameters, _ = curve_fit(
        Models.Model_Energy, xdata=x_data, ydata=y_data, p0=guess, bounds=BOUNDS)

    # evaluate the chi_2 function
    p1_fit = fit_parameters[0]
    p2_fit = fit_parameters[1]
    p3_fit = fit_parameters[2]

    th_data = Models.Model_Energy(x_data, p1_fit, p2_fit, p3_fit)
    chi2_fit = chi2(exp_data, th_data)
    return chi2_fit, [1.0/(2.0*p1_fit), 1.0/(2.0*p2_fit), 1.0/(2.0*p3_fit)], [p1_fit, p2_fit, p3_fit]


############################################################################
# fit for 136Nd higher  ####################################################
############################################################################
spins_136Nd_higher = np.concatenate(
    (Nd136.Spins_Band1_Higher, Nd136.Spins_Band2_Higher, Nd136.Spins_Band3_Higher))
phonons_136Nd_higher = np.concatenate(
    (Nd136.Phonons_Band1_Higher, Nd136.Phonons_Band2_Higher, Nd136.Phonons_Band3_Higher))
band_heads_136Nd_higher = np.asarray(
    [Nd136.Band_Head_Spin_Higher for _ in spins_136Nd_higher])
x_data_136Nd_higher = (
    spins_136Nd_higher, phonons_136Nd_higher, band_heads_136Nd_higher)
energies_exp_136Nd_higher = np.concatenate(
    (Nd136.Energy_Band1_Higher, Nd136.Energy_Band2_Higher, Nd136.Energy_Band3_Higher))
print('Higher')
print(do_fit(x_data_136Nd_higher, energies_exp_136Nd_higher,
      [1.0/(2.0*35), 1.0/(2.0*37), 1.0/(2.0*39)]))
############################################################################
############################################################################
############################################################################


############################################################################
# fit for 136Nd lower  ####################################################
############################################################################
spins_136Nd_lower = np.concatenate(
    (Nd136.Spins_Band1_Lower, Nd136.Spins_Band2_Lower))
phonons_136Nd_lower = np.concatenate(
    (Nd136.Phonons_Band1_Lower, Nd136.Phonons_Band2_Lower))
band_heads_136Nd_lower = np.asarray(
    [Nd136.Band_Head_Spin_Lower for _ in spins_136Nd_lower])
x_data_136Nd_lower = (
    spins_136Nd_lower, phonons_136Nd_lower, band_heads_136Nd_lower)
energies_exp_136Nd_lower = np.concatenate(
    (Nd136.Energy_Band1_Lower, Nd136.Energy_Band2_Lower))
print('Lower')
print(do_fit(x_data_136Nd_lower, energies_exp_136Nd_lower,
      [1.0/(2.0*35), 1.0/(2.0*37), 1.0/(2.0*39)]))
############################################################################
############################################################################
############################################################################
