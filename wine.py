#!/usr/bin/env python

import os
import numpy as np
from numpy import array
from numpy import vstack

def WineMain():
    np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
    y = np.loadtxt("wine.data.txt", delimiter=",")
    for idx, value in enumerate(y):
        print(idx,value)
    #print(y)
    #print("printed y above", y.shape)
    Part5Transpose(y)

def Part5Transpose(winenp):
    listTranspose = [[row[i] for row in winenp] for i in range( len(winenp[0]))]
    print ("\n . . . . .Part 5  Transpose. . . . . \n")
    for idx, value in enumerate(listTranspose):
        print(idx,value)
    Calculations(listTranspose)

def Calculations(features):
    print("Calculations")
    for idx, value in enumerate(features):
        print(value, "std=",np.std(value), "mean=", np.mean(value))
        #print(np.std(value))

print ("\n . . . . . W I N E . . . . . \n")
WineMain()
