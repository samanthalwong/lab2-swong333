import string
import numpy as np
import matplotlib.pyplot as plt

##add input and output + units to docstrings
def physconst(const):
    """Takes input (string) as the name of a physical constant and outputs its numerical value (float)"""

    const = const.lower()

    if (const == "c"):
        output = 2.99792458 * (10 ** (8))
    elif (const == "h"):
        output = 6.62606896 * (10 ** (-34))
    elif (const == "k"):
        output = 1.3806504 * (10 ** (-23))
    elif (const == "me"):
        output = 9.10938215 * (10 ** (-31))
    elif (const == "amu"):
        output = 1.660538782 * (10 ** (-27))
    elif (const == "e"):
        output == 1.602176487 * (10 ** (-19))
    elif (const == "a0"):
        output = 5.2917720859 * (10 ** (-11))
    elif (const == "g"):
        output = 6.67428 * (10 ** (-11))
    elif (const == "sigma"):
        output = 5.670400 * (10 ** (-8))
    else:
        print("The value entered was invalid")
    return output


def planck(temperatures, frequencies):
    """Takes input of a 1D numpy array of temperatures and frequencies (integers).
    Returns the 2D numpy array consisting of the Planck radiation at each of the input values (floats)"""

    #use physconst function to get h, c, k
    h = physconst("h")
    c = physconst("c")
    k = physconst("k")

    #assign temperatures to each row of the matrix
    temperatures = temperatures[:, np.newaxis]

    #calculate planck function in steps to make it easier to check
    x=(2*h*np.power(frequencies,3))/c**2
    y=h*frequencies/(k*temperatures)
    z = np.exp(y) - 1
    zz = np.power(z, -1)
    boltz_matrix = x*zz

    return boltz_matrix

#given values, convert from wavelength to frequency
temps = np.array([5000, 10000, 15000])
lambdas = np.arange(10, 2001)
freqs = np.divide(physconst("c"), (lambdas / 10 ** 9))

#radiation values for each temperature (row)
y1 = planck(temps, freqs)[0, :]
y2 = planck(temps, freqs)[1, :]
y3 = planck(temps, freqs)[2, :]

plt.plot(y1, 'b', y2,'r', y3, 'k')
plt.legend(['T = 5000 K','T = 10 000 K','T = 15 000 K'])
plt.xlabel("Frequency of Light (Hz)")
plt.ylabel("Intensity")
plt.title("Radiation Field for T = 5000K, 10 000K, and 15 0000K for Light in a Vacuum")

plt.show()

#check that function is correct with numpy.trapz
int1 = np.trapz(freqs,y1)
int2 = np.trapz(freqs,y2)
int3 = np.trapz(freqs,y3)
line1 = np.array([int1,int2,int3])

#find the s-b result for each temperature
sb_law1 = physconst("sigma")*(5000**4)/np.pi
sb_law2 = physconst("sigma")*(10000**4)/np.pi
sb_law3 = physconst("sigma")*(15000**4)/np.pi
line2 = np.array([sb_law1,sb_law2,sb_law3])

#calculate error
err1 = 100 - (sb_law1/int1 * 100)
err2 = 100 - (sb_law2/int2 * 100)
err3 = 100 - (sb_law3/int3 * 100)

#table with comparison data-
#didn't know how to make a table without a graph so sorry about the graph axes in the background
table_data = ([int1,int2,int3],[sb_law1,sb_law2,sb_law3],[err1,err2,err3])
rows = ("Planck Radiation Function", "Stefan-Boltzmann Equation", "Error of Planck Function (%)")
cols = ("T = 5000 K", "T = 10 000 K", "T = 15 000 K")
plt.table(cellText=table_data, rowLabels=rows, colLabels=cols, loc="center")
plt.title("Comparison of Planck Function Values vs. Calculated Stefan-Boltzmann Equation Values with Error of Planck Results")
plt.show()
