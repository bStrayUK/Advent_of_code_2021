# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 13:17:50 2021

@author: Ben
"""

import numpy as np

crabOriginalPos = np.loadtxt("Day7input.txt",delimiter=',')
#crabOriginalPos = [16,1,2,0,4,2,7,1,2,14]

maxPosition = max(crabOriginalPos)
minFuel = maxPosition*len(crabOriginalPos) # Some large number to be overwritten
bestPos = 0

for x in np.arange(maxPosition):
    fuel = 0
    while fuel < minFuel:
        for crab in crabOriginalPos:
            fuel += abs(x-crab)
        if fuel < minFuel:
            minFuel = fuel
            bestPos = x
            print("New best fuel and position:")
            print(minFuel,bestPos)
print("-----------------------------")
print("Final best fuel and position:")
print(minFuel,bestPos)


# Part 2
maxPosition = max(crabOriginalPos)
minFuel = maxPosition*len(crabOriginalPos)*maxPosition*maxPosition # Some large number to be overwritten
bestPos = 0

for x in np.arange(maxPosition):
    fuel = 0
    while fuel < minFuel:
        for crab in crabOriginalPos:
            fuel += sum(np.arange(abs(x-crab)+1))
        if fuel < minFuel:
            minFuel = fuel
            bestPos = x
            print("New best fuel and position:")
            print(minFuel,bestPos)

print("-----------------------------")
print("Final best fuel and position:")
print(minFuel,bestPos)