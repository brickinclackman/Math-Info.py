import numpy as np
from termcolor import colored

def Create_M_Identity(n):
    i = np.zeros((n,n))
    for index in range(n):
        i[index][index] = 1
    return i

def nombre