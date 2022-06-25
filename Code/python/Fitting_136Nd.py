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
    return chi


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


def do_fit_higher(guess):
    fit_parameters_136Nd_higher, _ = curve_fit(
        Models.Model_Energy, x_data_136Nd_higher, energies_exp_136Nd_higher, p0=guess, bounds=BOUNDS)

    # evaluate the chi_2 function
    e1_higher = fit_parameters_136Nd_higher[0]
    e2_higher = fit_parameters_136Nd_higher[1]
    e3_higher = fit_parameters_136Nd_higher[2]
    # print(1/(2.0*e1_higher))
    # print(1/(2.0*e2_higher))
    # print(1/(2.0*e3_higher))
    x = chi2(energies_exp_136Nd_higher, Models.Model_Energy(
        x_data_136Nd_higher, e1_higher, e2_higher, e3_higher))
    return x, [e1_higher, e2_higher, e3_higher]


min_chi = Models.MAX_VAL
for i1 in np.arange(10, 125, 15):
    for i2 in np.arange(11, 125, 15):
        for i3 in np.arange(12, 125, 15):
            # if(i1 != i2):
            #     if(i1 != i3):
            #         if(i2 != i3):
            #             guess_i = [1.0/(2.0*i1), 1.0/(2.0*i2), 1.0/(2.0*i3)]
            #             chi_i = do_fit_higher(guess_i)[0]
            #             mois_i = do_fit_higher(guess_i)[1]
            #             if(chi_i < min_chi):
            #                 print([1.0/(2.0*e) for e in mois_i])
            #                 min_chi = chi_i
            guess_i = [1.0/(2.0*i1), 1.0/(2.0*i2), 1.0/(2.0*i3)]
            chi_i = do_fit_higher(guess_i)[0]
            mois_i = do_fit_higher(guess_i)[1]
            if(chi_i < min_chi):
                print([1.0/(2.0*e) for e in mois_i], chi_i)
                min_chi = chi_i


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


def do_fit_lower(guess):
    fit_parameters_136Nd_lower, _ = curve_fit(
        Models.Model_Energy, x_data_136Nd_lower, energies_exp_136Nd_lower, p0=guess, bounds=BOUNDS)

    # evaluate the chi_2 function
    e1_lower = fit_parameters_136Nd_lower[0]
    e2_lower = fit_parameters_136Nd_lower[1]
    e3_lower = fit_parameters_136Nd_lower[2]
    # print(1/(2.0*e1_lower))
    # print(1/(2.0*e2_lower))
    # print(1/(2.0*e3_lower))
    x = chi2(energies_exp_136Nd_lower, Models.Model_Energy(
        x_data_136Nd_lower, e1_lower, e2_lower, e3_lower))
    return x, [e1_lower, e2_lower, e3_lower]


min_chi = Models.MAX_VAL
for i1 in np.arange(10, 125, 15):
    for i2 in np.arange(11, 125, 15):
        for i3 in np.arange(12, 125, 15):
            guess_i = [1.0/(2.0*i1), 1.0/(2.0*i2), 1.0/(2.0*i3)]
            chi_i = do_fit_lower(guess_i)[0]
            mois_i = do_fit_lower(guess_i)[1]
            if(chi_i < min_chi):
                print([1.0/(2.0*e) for e in mois_i], chi_i)
                min_chi = chi_i
