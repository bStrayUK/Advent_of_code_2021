# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 15:23:15 2021

@author: Ben
"""

import numpy as np

inputs = np.loadtxt("Day3input.txt",dtype=str)

epsilon = ''
gamma = ''

for index in np.arange(0,12):
    ones = 0
    zeros = 0
    for i,v in enumerate(inputs):
        if inputs[i][2+index] == '1':
            ones += 1
        elif inputs[i][2+index] == '0':
            zeros += 1
        else:
            print("Ben, you messed up dawg")
    
    if ones > zeros:
        gamma += '1'
        epsilon += '0'
    elif zeros > ones:
        gamma += '0'
        epsilon += '1'

gammaNum = int(gamma,base=2)
epsilonNum = int(epsilon,base=2)

print("Power consumption is")
print(gammaNum*epsilonNum)

oxygen = ''
co2 = ''

newList = inputs
for index in np.arange(0,12):
    dummyList = []
    ones = 0
    zeros = 0
    for i,v in enumerate(newList):
        if newList[i][2+index] == '1':
            ones += 1
        elif newList[i][2+index] == '0':
            zeros += 1
        else:
            print("Ben, you messed up dawg")
    
    if ones > zeros:
        for i,v in enumerate(newList):
            if newList[i][2+index] == '1':
                dummyList.append(newList[i])
    elif zeros > ones:
        for i,v in enumerate(newList):
            if newList[i][2+index] == '0':
                dummyList.append(newList[i])
    
    elif ones == zeros:
        for i,v in enumerate(newList):
            if newList[i][2+index] == '1':
                dummyList.append(newList[i])
    
    newList = dummyList
#    print(newList)
    
    if len(newList) == 1:
        oxygen = int(newList[0][2:-1],base=2)
        print("Oxygen")
        print(oxygen)

newList = inputs
for index in np.arange(0,12):
    dummyList = []
    ones = 0
    zeros = 0
    for i,v in enumerate(newList):
        if newList[i][2+index] == '1':
            ones += 1
        elif newList[i][2+index] == '0':
            zeros += 1
        else:
            print("Ben, you messed up dawg")
    
    if ones < zeros:
        for i,v in enumerate(newList):
            if newList[i][2+index] == '1':
                dummyList.append(newList[i])
    elif zeros < ones:
        for i,v in enumerate(newList):
            if newList[i][2+index] == '0':
                dummyList.append(newList[i])
    
    elif ones == zeros:
        for i,v in enumerate(newList):
            if newList[i][2+index] == '0':
                dummyList.append(newList[i])
    
    newList = dummyList
#    print(newList)
    
    if len(newList) == 1:
        co2 = int(newList[0][2:-1],base=2)
        print("CO2")
        print(co2)
        
print("Life support")
print(oxygen*co2)