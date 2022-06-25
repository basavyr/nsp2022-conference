import numpy as np


# the experimental data for the 10^+ isomer
# two wobbling bands (n=0,1) built on top of I=10^+ isomer state
# the two wobbling bands are labelled as "8" and "10" in "Transverse wobbling motion in 134 Ce and 136Nd, C. M. Petrache, S. Guo"
# n=0 ground-state decays to 8^+ from band "1"

# experimental data for the set of bands 8-10 (the 10^+ isomer structure)
band8_energy_exp = sorted([7550, 6776, 5864, 4761, 4006, 3207])
band10_energy_exp = sorted([6523, 5492, 4697])
band8_spins = np.arange(10, 22, 2)
band10_spins = np.arange(13, 19, 2)
band8_band_head_energy = band8_energy_exp[0]
band8_band_head_spin = band8_spins[0]


# experimental data for set of bands 9-7 (the highly-deformed 10^+ level)
band9_energy_exp = sorted([8583, 7581, 6597, 5724, 4907, 4183, 3719])
band7_energy_exp = sorted([5717, 4924, 4384])
band9_spins = np.arange(10, 24, 2)
band7_spins = np.arange(11, 17, 2)
band9_band_head_energy = band9_energy_exp[0]
band9_band_head_spin = band9_spins[0]


def MeV(energy):
    """
    Transform the energy from keV to MeV
    """
    return np.round(energy / 1000.0, 3)


# final nomenclature that will be used within the fitting procedure
Energy_Band1_Isomer = [MeV(e-band8_band_head_energy)
                       for e in band8_energy_exp[1:]]
Energy_Band2_Isomer = [MeV(e-band8_band_head_energy)
                       for e in band10_energy_exp]
Spins_Band1_Isomer = band8_spins[1:]
Spins_Band2_Isomer = band10_spins
Phonons_Band1_Isomer = [0 for _ in Energy_Band1_Isomer]
Phonons_Band2_Isomer = [1 for _ in Energy_Band2_Isomer]
Energy_Band_Head_Isomer = band8_band_head_energy
Spin_Band_Head_Isomer = band8_band_head_spin

Energy_Band1_Deformed = [MeV(e-band9_band_head_energy)
                         for e in band9_energy_exp[1:]]
Energy_Band2_Deformed = [MeV(e-band9_band_head_energy)
                         for e in band7_energy_exp]
Spins_Band1_Deformed = band9_spins[1:]
Spins_Band2_Deformed = band7_spins
Phonons_Band1_Deformed = [0 for _ in Energy_Band1_Deformed]
Phonons_Band2_Deformed = [1 for _ in Energy_Band2_Deformed]
Energy_Band_Head_Deformed = band9_band_head_energy
Spin_Band_Head_Deformed = band9_band_head_spin
