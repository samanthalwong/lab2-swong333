import string
import numpy as np
import matplotlib.pyplot as plt


def physconst(const):
    """Takes input as the name of a physical constant and outputs its numerical value"""

    const = const.lower()

    if (const == "speed of light"):
        output = 2.99792458 * 10 ** (8)
    elif (const == "planck's constant"):
        output = 6.62606896 * 10 ** (-34)
    elif (const == "boltzmann's constant"):
        output = 1.3806504 * 10 ** (-23)
    elif (const == "electron mass"):
        output = 9.10938215 * 10 ** (-31)
    elif (const == "atomic mass unit"):
        output = 1.660538782 * 10 ** (-27)
    elif (const == "electron charge"):
        output == 1.602176487 * 10 ** (-19)
    elif (const == "bohr radius"):
        output = 5.2917720859 * 10 ** (-11)
    elif (const == "gravitational constant"):
        output = 6.67428 * 10 ** (-11)
    elif (const == "stefan-boltzmann constant"):
        output = 5.670400 * 10 ** (-8)
    else:
        print("The value entered was invalid")
    return output


def planck(temperatures, frequencies):
    """Returns the physical constants that compute the Planck radiation function"""
    h = physconst("planck's constant")
    c = physconst("speed of light")
    k = physconst("boltzmann's constant")
    temperatures = temperatures[:, np.newaxis]

    x = (np.multiply((2*h),(np.power(frequencies, 3))))/(c**2)
    #print(x)
    y = np.divide(np.multiply(h, frequencies), np.multiply(k, temperatures))
    print(y)
    z = np.exp(y) - 1
    #print(z)
    zz = np.power(z, -1)

    boltz_matrix = x*zz

    #boltz_matrix = ((2 * h * (np.power(frequencies, 3))) / (c ** 2)) * ((np.exp((np.multiply(h, frequencies)) / (np.multiply(k, temperatures))) - 1) ** (-1))
    return boltz_matrix


temps = np.array([5000, 10000, 15000])
lambdas = np.arange(10, 2001)
freqs = np.divide(physconst("speed of light"), (lambdas / 10 ** 9))

print(planck(temps, freqs))
