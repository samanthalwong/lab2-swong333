# Lab 2: Physical constants
## Skills: functions, strings, numerical integration, version control

### Background
A pre-requisite to scientific programming in physics or astronomy is some way to manage the various physical constants. One possible approach is to define the required constants in each function where they are required. However, this approach is error-prone, and it is very difficult to update the physical constants as revised values
are published (although, admittedly, the changes are now tiny). In this lab, you will look at an approach to solving this problem, code it, and then using your function, write a  function to compute the Planck function _B<sub>&nu;</sub>(T)_. The Python packages `astropy` and `scipy` already have this functionality, but the point of this lab is for you to develop it yourself. You can use `astropy.constants`, `scipy.constants` and/or `astropy.modeling.blackbody` to check your code's results if you like, but don't use them in implementing your code.


One possible way to manage the physical constants in a reasonable way is to construct a function that accepts as an argument a string variable and returns as output the physical constant associated with that string. For example `CC = physconst(’c’)` recognizes the string `c` as associated with the speed of light and returns its numerical value, which is then assigned to `CC`. Calls to this function can then be used by other functions to set the physical constants in a consistent way. A minimal set of constants that you will need for this course are given in the table below, in SI units.

Starting with this lab, you must use version control as you develop your programs. This means writing your code as a series of small changes, and committing those changes to the repository that you eventually submit. The best way to do this is to work in a development environment that integrates with git and GitHub. Your final repository should have at least one commit for each part of the lab. 


### Part 1
Write a function `physconst` that takes as input the name of a physical constant and returns its numerical value, as given in the table below. Your function should include some minimal documentation in the form of a [docstring](https://www.pythonforbeginners.com/basics/python-docstrings).

Upper/lower/mixed case for the calling strings should be allowed (check out the relevant string functions), and you should trap obvious errors in the user input. In writing this function, you may find Python `if-elif-else` statements and/or Python *dictionaries* useful. **Submit this function in the `assign.py` file in your repository.**

| Constant | Symbol | String | SI value | units |
| -------- | ------ | ------ | -------- | ----- |
| speed of light| _c_ | `c` | 2.99792458e8 | m s<sup>-1</sup> |
| Planck’s Constant | _h_ | `h` | 6.62606896e−34 | J s|
| Boltzmann’s Constant | _k_ | `k` | 1.3806504e−23 | J K<sup>-1</sup> |
| Electron Mass | _m<sub>e</sub>_ | `Me` | 9.10938215e−31 | kg |
| Atomic Mass Unit | _u_ | `amu` | 1.660538782e−27 | kg |
| Electron Charge | _e_ | `e` | 1.602176487e−19 | C |
| Bohr Radius | _a<sub>0</sub>_ | `a0` | 5.2917720859e−11 | m |
| Gravitational Constant | _G_ | `G` | 6.67428e−11 | N m<sup>2</sup> kg<sup>-2</sup> |
| Stefan-Boltzmann Constant | &sigma; | `Sigma` | 5.670400e−8 | W m<sup>-2</sup> K<sup>-4</sup> |

### Part 2 
Use your function to return the physical constants in a Python function `planck` (with a docstring) that computes the Planck radiation
function,

 _B<sub>&nu;</sub>(T) = (2h &nu;<sup>3</sup>/c<sup>2</sup>)_ * (exp _(h &nu;/kT) − 1)_<sup>-1</sup>

Here _&nu;_ is the frequency of light (in Hz) and _T_ is the temperature (in K). All of the other symbols are physical constants with the usual meanings. In your function call, you must allow for 1-D array of temperatures and 1-D array of frequencies to be given. If M temperatures and N frequencies are given, your function should return an N-by-M array where the rows correspond to a single temperature and the columns, a single frequency.  Your function cannot contain any looping constructs (such as for-loops or while- loops) to achieve this functionality. (Hint: look up the concept of *broadcasting* in Python documentation). **Submit this function in the `assign.py` file in your repository.**

### Part 3
Use your Planck function to plot up the radiation field from _&lambda;_ = 10 to 2000 nm for the three temperatures _T = 5000, 10000, 15000_ K. Note that _&lambda; &nu; = c_ for light in a vacuum. Plot all three curves on the same figure with a legend. **Save the figure to a file and add it to your repository. The code that makes the plot should be included in the `assign2.py` file.**

### Part 4
For any function you write, it is a good idea to test it carefully to ensure it works correctly. The basis of one possible test for your Planck function is the well-known Stefan-Boltzmann radiation law which states that

&int;<sub>0</sub><sup>&infin;</sup>  B<sub>&nu;</sub>(T) d&nu; = &sigma; T<sup>4</sup>/&pi;

where &sigma; is the Stefan-Boltzmann constant above. Use the `numpy.trapz` function to verify that your Planck function reproduces this law. Make a table or plot to demonstrate this; include the table or plot in your repository. **The code that does the verification should be included in the `assign2.py` file.**
