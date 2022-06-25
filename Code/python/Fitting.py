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


############################################################################
# fit for 134Ce ############################################################
############################################################################
spins_134Ce_isomer=np.concatenate((Ce134.Spins_Band1_Isomer,Ce134.Spins_Band2_Isomer))
phonons_134Ce_isomer=np.asarray(Ce134.Phonons_Band1_Isomer+Ce134.Phonons_Band2_Isomer)
x_data_134Ce_isomer=(spins_134Ce_isomer,phonons_134Ce_isomer)
experimental_energies_134Ce_isomer=np.asarray(Ce134.Energy_Band1_Isomer+Ce134.Energy_Band2_Isomer)
guess134Ce_isomer=[0.8,0.5,0.1]
fit_parameters_134Ce_isomer, _=curve_fit(Models.Model_Energy,x_data_134Ce_isomer,experimental_energies_134Ce_isomer,p0=guess134Ce_isomer,bounds=BOUNDS)
print(fit_parameters_134Ce_isomer)
############################################################################
############################################################################
############################################################################