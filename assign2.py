import string
import numpy as np
import matplotlib.pyplot as plt

def physconst(input):
  """Takes input as the name of a physical constant and outputs its numerical value"""

  input = input.lower

  if(input == "speed of light"):
    output = 2.99792458e8
  elif (input == "planck's constant"):
    output = 6.62606896e−34	
  elif (input == "boltzmann's constant"):
    output = 1.3806504e−23	
  elif (input == "electron mass"):
    output = 9.10938215e−31
  elif (input == "atomic mass unit"):
    output = 1.660538782e−27	
  elif (input == "electron charge"):
    output == 1.602176487e−19
  elif (input == "bohr radius"):
    output = 5.2917720859e−11
  elif (input == "gravitational constant"):
    output = 6.67428e−11
  elif (input == "stefan-boltzmann constant"):
    output = 5.670400e−8
  else:
    print("The value entered was invalid")
  return output


def planck():
  """Function docstring goes here.""" 
  return()
