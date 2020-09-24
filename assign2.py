import string
import numpy as np
import matplotlib.pyplot as plt

##add input and output + units to docstrings
def physconst(const):
    """Takes input as the name of a physical constant and outputs its numerical value"""

    const = const.lower()

    if (const == "speed of light"):
        output = 2.99792458 * (10 ** (8))
    elif (const == "planck's constant"):
        output = 6.62606896 * (10 ** (-34))
    elif (const == "boltzmann's constant"):
        output = 1.3806504 * (10 ** (-23))
    elif (const == "electron mass"):
        output = 9.10938215 * (10 ** (-31))
    elif (const == "atomic mass unit"):
        output = 1.660538782 * (10 ** (-27))
    elif (const == "electron charge"):
        output == 1.602176487 * (10 ** (-19))
    elif (const == "bohr radius"):
        output = 5.2917720859 * (10 ** (-11))
    elif (const == "gravitational constant"):
        output = 6.67428 * (10 ** (-11))
    elif (const == "stefan-boltzmann constant"):
        output = 5.670400 * (10 ** (-8))
    else:
        print("The value entered was invalid")
    return output


def planck(temperatures, frequencies):
    """Returns the physical constants that compute the Planck radiation function"""
    h = physconst("planck's constant")
    c = physconst("speed of light")
    k = physconst("boltzmann's constant")
    temperatures = temperatures[:, np.newaxis]

    x=(2*h*np.power(frequencies,3))/c**2

    y=h*frequencies/(k*temperatures)

    z = np.exp(y) - 1

    zz = np.power(z, -1)
    boltz_matrix = x*zz

    return boltz_matrix


temps = np.array([5000, 10000, 15000])
lambdas = np.arange(10, 2001)
freqs = np.divide(physconst("speed of light"), (lambdas / 10 ** 9))

y1 = planck(temps, freqs)[0, :]
y2 = planck(temps, freqs)[1, :]
y3 = planck(temps, freqs)[2, :]

plt.plot(y1, 'b', y2,'r', y3, 'k')
plt.legend(['T = 5000 K','T = 10 000 K','T = 15 000 K'])
plt.xlabel("Frequency of Light (Hz)")
plt.ylabel("Intensity")
plt.title("Radiation Field for T = 5000K, 10 000K, and 15 0000K for Light in a Vacuum")

#plt.show()

#check that function is correct with numpy.trapz
int1 = np.trapz(freqs,y1)
int2 = np.trapz(freqs,y2)
int3 = np.trapz(freqs,y3)

sb_law1 = physconst("stefan-boltzmann constant")*(5000**4)/np.pi
sb_law2 = physconst("stefan-boltzmann constant")*(10000**4)/np.pi
sb_law3 = physconst("stefan-boltzmann constant")*(15000**4)/np.pi



print(sb_law1,sb_law2,sb_law3)
print(int1, int2, int3)
