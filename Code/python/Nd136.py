import numpy as np


def MeV(energy):
    """
    Transform the energy from keV to MeV
    """
    return np.round(energy / 1000.0, 3)


# experimental data for 136Nd
# the isotope has two wobbling structures
# Structure 1: bands "2" "5" and "6" are the n_w=0,1,2 wobbling bands
# Structure 2: bands "3" and "4" are the n_w=0,1 wobbling bands
# both structures decay into the 8^+ level from band "1"
# both bands have the band-head (first spin state from the ground-band) as 10^+
# Structure 1 has a lower energy for the 10^+ state

band3_spins = np.arange(10, 18, 2)
band3_energy_exp = sorted([5841, 4847, 3995, 3277])
band4_spins = np.arange(11, 17, 2)
band4_energy_exp = sorted([5346, 4545, 4026])


band2_spins = np.arange(10, 24, 2)
band2_energy_exp = sorted([8615, 7349, 6188, 5189, 4345, 3684, 3294])
band5_spins = np.arange(13, 23, 2)
band5_energy_exp = sorted([8098, 6928, 5940, 5130, 4452])
band6_spins = np.arange(14, 26, 2)
band6_energy_exp = sorted([9171, 8222, 7329, 6470, 5568, 4853])

# data for Structure 1
Spins_Band1_Lower = band3_spins[1:]
Spins_Band2_Lower = band4_spins
Band_Head_Spin_Lower = band3_spins[0]
Band_Head_Energy_Lower = band3_energy_exp[0]
Energy_Band1_Lower = np.asarray(
    [MeV(e-Band_Head_Energy_Lower) for e in band3_energy_exp[1:]])
Energy_Band2_Lower = np.asarray(
    [MeV(e-Band_Head_Energy_Lower) for e in band4_energy_exp])

# data for Structure 2
Spins_Band1_Higher = band2_spins[1:]
Spins_Band2_Higher = band5_spins
Spins_Band3_Higher = band6_spins
Band_Head_Spin_Higher = band2_spins[0]
Band_Head_Energy_Higher = band2_energy_exp[0]
Energy_Band1_Higher = np.asarray(
    MeV([e-Band_Head_Energy_Higher]) for e in band2_energy_exp[1:])
Energy_Band2_Higher = np.asarray(
    MeV([e-Band_Head_Energy_Higher]) for e in band5_energy_exp)
Energy_Band3_Higher = np.asarray(
    MeV([e-Band_Head_Energy_Higher]) for e in band6_energy_exp)
