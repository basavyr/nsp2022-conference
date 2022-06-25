import numpy as np
from scipy.optimize import curve_fit


import Energies as Models


# add limits for the inertia factors
A_MIN = 0.004
A_MAX = 1.0
# these limits correspond to 1<=MOI<=125 \hbar^2MeV^-1
