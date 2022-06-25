from ntpath import join
import numpy as np
from scipy.optimize import curve_fit


import Energies as Models
import Ce134

# add limits for the inertia factors
# these limits correspond to 1<=MOI<=125 \hbar^2MeV^-1
A_MIN = 0.004
A_MAX = 1.0
BOUNDS = ([A_MIN,A_MIN,A_MIN], [A_MAX,A_MAX,A_MAX])


def chi2(exp_data,th_data):
    sum_0=0
    for i in range(len(exp_data)):
        e=np.power(exp_data[i]-th_data[i],2)
        sum_0+=e/exp_data[i]
    chi=1.0/len(exp_data+1)*sum_0
    print(np.sqrt(chi))
    # return np.sqrt(chi)


############################################################################
# fit for 134Ce isomer #####################################################
############################################################################
spins_134Ce_isomer=np.concatenate((Ce134.Spins_Band1_Isomer,Ce134.Spins_Band2_Isomer))
phonons_134Ce_isomer=np.asarray(Ce134.Phonons_Band1_Isomer+Ce134.Phonons_Band2_Isomer)
band_heads_134Ce_isomer=np.asarray([Ce134.Spin_Band_Head_Isomer for _ in range(len(spins_134Ce_isomer))])

x_data_134Ce_isomer=(spins_134Ce_isomer,phonons_134Ce_isomer,band_heads_134Ce_isomer)

experimental_energies_134Ce_isomer=np.asarray(Ce134.Energy_Band1_Isomer+Ce134.Energy_Band2_Isomer)
guess134Ce_isomer=[0.8,0.5,0.1]

fit_parameters_134Ce_isomer, _=curve_fit(Models.Model_Energy,x_data_134Ce_isomer,experimental_energies_134Ce_isomer,p0=guess134Ce_isomer,bounds=BOUNDS)

#evaluate the chi_2 function
e1_isomer=fit_parameters_134Ce_isomer[0]
e2_isomer=fit_parameters_134Ce_isomer[1]
e3_isomer=fit_parameters_134Ce_isomer[2]
chi2(experimental_energies_134Ce_isomer,Models.Model_Energy(x_data_134Ce_isomer,e1_isomer,e2_isomer,e3_isomer))
############################################################################
############################################################################
############################################################################

############################################################################
# fit for 134Ce high deformation ###########################################
############################################################################
spins_134Ce_deformed=np.concatenate((Ce134.Spins_Band1_Deformed,Ce134.Spins_Band2_Deformed))
phonons_134Ce_deformed=np.asarray(Ce134.Phonons_Band1_Deformed+Ce134.Phonons_Band2_Deformed)
band_heads_134Ce_deformed=np.asarray([Ce134.Spin_Band_Head_Deformed for _ in range(len(spins_134Ce_deformed))])

x_data_134Ce_deformed=(spins_134Ce_deformed,phonons_134Ce_deformed,band_heads_134Ce_deformed)

experimental_energies_134Ce_deformed=np.asarray(Ce134.Energy_Band1_Deformed+Ce134.Energy_Band2_Deformed)
guess134Ce_deformed=[0.8,0.5,0.1]

fit_parameters_134Ce_deformed, _=curve_fit(Models.Model_Energy,x_data_134Ce_deformed,experimental_energies_134Ce_deformed,p0=guess134Ce_deformed,bounds=BOUNDS)

#evaluate the chi_2 function
e1_deformed=fit_parameters_134Ce_deformed[0]
e2_deformed=fit_parameters_134Ce_deformed[1]
e3_deformed=fit_parameters_134Ce_deformed[2]
chi2(experimental_energies_134Ce_deformed,Models.Model_Energy(x_data_134Ce_deformed,e1_deformed,e2_deformed,e3_deformed))
############################################################################
############################################################################
############################################################################