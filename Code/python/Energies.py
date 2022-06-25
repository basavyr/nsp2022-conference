import math
import numpy as np

# escape value to be used in case of math failure
MAX_VAL = 6969696969


def Wobbling_Frequency(spin, A1, A2, A3):
    # stopping conditions for un-physical solutions
    if(A1 < 0.0):
        return MAX_VAL
    if(A2 < 0.0):
        return MAX_VAL
    if(A3 < 0.0):
        return MAX_VAL
    if(A1 == 0):
        return MAX_VAL
    if(A2 == 0):
        return MAX_VAL
    if(A3 == 0):
        return MAX_VAL
    if(A1 < A3 and A2 > A3):
        return MAX_VAL
    if(A1 > A3 and A2 < A3):
        return MAX_VAL

    I = spin

    t1 = I*(A2+A1-2.0*A3)
    t2 = I*(A2-A1)
    t1_2 = np.power(t1, 2)
    t2_2 = np.power(t2, 2)

    if(t1_2 <= t2_2):
        return MAX_VAL

    h_omega_wob = np.sqrt(t1_2-t2_2)

    return h_omega_wob


def Absolute_Energy(spin, phonon_number, A1, A2, A3):
    if(A3 == 0):
        return MAX_VAL

    I = spin
    n = phonon_number

    h_omega_wob = Wobbling_Frequency(I, A1, A2, A3)
    if(h_omega_wob == MAX_VAL):
        return MAX_VAL

    rotation_term = A3*I*(I+1.0)
    harmonic_term = h_omega_wob*(n+0.5)

    energy = rotation_term+harmonic_term

    return energy


def Excitation_Energy(spin, phonon_number, band_head_absolute_energy, A1, A2, A3):
    """
    Calculate the excitation energy for a given state 
    The excitation energy is evaluated as the difference between the absolute energy of that state and the band-head energy
    The function should have band-head spin as an argument
    """

    # I_0 = band_head_spin

    # # first evaluate the energy of the band head
    # E_0 = Absolute_Energy(I_0, 0, A1, A2, A3)
    # if(E_0 == MAX_VAL):
    #     return MAX_VAL

    I = spin
    n = phonon_number
    E_0 = band_head_absolute_energy

    # evaluate the absolute energy of the I level state
    E_I = Absolute_Energy(I, n, A1, A2, A3)
    if(E_I == MAX_VAL):
        return MAX_VAL

    return E_I-E_0


def Model_Energy(x_data, band_head_absolute_energy, A1, A2, A3):
    """
    the model function that will be used in the curve_fit  
    the function must be capable of dealing with arrays for the spin and the phonon number
    """

    # unpack the x-data in terms of the spins and the phonon numbers
    spins, phonons = x_data

    E_0 = band_head_absolute_energy
    local_energies = Excitation_Energy(spins, phonons, E_0, A1, A2, A3)

    return local_energies
