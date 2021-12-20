# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 20:07:44 2021

@author: Ben
"""
import numpy as np

with open('Day8input.txt') as f:
    inputOutputs= f.readlines()

inputOutputs = np.array([inOut.replace('\n','').split(' ') for inOut in inputOutputs])

# Split the inputs from the outputs
digitIn = inputOutputs[:,0:10]
digitOut = inputOutputs[:,11:]

# Dumb way to store count digits
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0
sevens = 0
eights = 0
nines = 0
zeros = 0

totalSum = 0

for index, value in enumerate(digitIn):
    digitDict = {}

    # First loop through to find the unique values
    for inin, valval in enumerate(value):
        valen = len(valval)

        if valen == 2:
            digitDict[1] = valval # one
        elif valen == 3:
            digitDict[7] = valval # seven
        elif valen == 4:
            digitDict[4] = valval # four
        elif valen == 7:
            digitDict[8] = valval # eight
     # Find the len 6 values using the uniques
    for inin, valval in enumerate(value):
        valen = len(valval)
        if valen == 6:
            if all([x in valval for x in list(digitDict[4])]):
                digitDict[9] = valval
            # see if the bars from number 1 are in the digit, if so it is 0, else it is 6
            elif all([x in valval for x in list(digitDict[1])]):
                digitDict[0] = valval
            else:
                digitDict[6] = valval
    # Find the len 5 values using the uniques and other found numbers
    for inin, valval in enumerate(value):
        valen = len(valval)
        if valen == 5:
            if all([x in valval for x in list(digitDict[7])]):
                digitDict[3] = valval
            elif all([x in digitDict[6] for x in list(valval)]):
                digitDict[5] = valval
            else:
                digitDict[2] = valval

    # Decode the output
    outputNum = 0
    # Since output is four digit number, use decoded num, n, times by the factor 1000/10**ind and sum the number
    for ind, outval in enumerate(digitOut[index]):
        # Remove the ones, then check every entry in length order to avoid incorrectly counting
        if outval == digitDict[1] or outval == digitDict[1][::-1]:
            ones += 1
            outputNum += 1*1000/10**ind
        elif all([x in outval for x in list(digitDict[8])]):
            eights += 1
            outputNum += 8*1000/10**ind
        elif all([x in outval for x in list(digitDict[6])]):
            sixes += 1
            outputNum += 6*1000/10**ind
        elif all([x in outval for x in list(digitDict[0])]):
            zeros += 1
            outputNum += 0*1000/10**ind
        elif all([x in outval for x in list(digitDict[9])]):
            nines += 1
            outputNum += 9*1000/10**ind
        elif all([x in outval for x in list(digitDict[2])]):
            twos += 1
            outputNum += 2*1000/10**ind
        elif all([x in outval for x in list(digitDict[5])]):
            fives += 1
            outputNum += 5*1000/10**ind
        elif all([x in outval for x in list(digitDict[3])]):
            threes += 1
            outputNum += 3*1000/10**ind
        elif all([x in outval for x in list(digitDict[4])]):
            fours += 1
            outputNum += 4*1000/10**ind
        elif all([x in outval for x in list(digitDict[7])]):
            sevens += 1
            outputNum += 7*1000/10**ind

    totalSum += outputNum


# Part 1
print("Number of 1,4,7,8:")
print(sum([ones,fours,sevens,eights]))
print("All numbers:")
print(ones,twos,threes,fours,fives,sixes,sevens,eights,nines,zeros)

# Part 2
print('Total sum of all outputs:')
print(totalSum)
