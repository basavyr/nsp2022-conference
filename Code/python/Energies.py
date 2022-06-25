import math

# escape value to be used in case of math failure
MAXVAL = 6969696969


def MeV(energy):
    """
    Transform the energy from keV to MeV
    """
    return np.round(energy / 1000.0, 3)