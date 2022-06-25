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


guess136Nd_lower = [1.0/(2.0*10.0), 1.0/(2.0*25.0), 1.0/(2.0*1.0)]

fit_parameters_136Nd_higher, _ = curve_fit(
    Models.Model_Energy, x_data_136Nd_higher, energies_exp_136Nd_higher, p0=guess136Nd_lower, bounds=BOUNDS)

# evaluate the chi_2 function
e1_higher = fit_parameters_136Nd_higher[0]
e2_higher = fit_parameters_136Nd_higher[1]
e3_higher = fit_parameters_136Nd_higher[2]
print(1/(2.0*e1_higher))
print(1/(2.0*e2_higher))
print(1/(2.0*e3_higher))
chi2(energies_exp_136Nd_higher, Models.Model_Energy(
    x_data_136Nd_higher, e1_higher, e2_higher, e3_higher))
############################################################################
############################################################################
############################################################################


############################################################################
# fit for 136Nd lower  ####################################################
############################################################################