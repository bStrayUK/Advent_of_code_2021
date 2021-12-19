# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 13:17:50 2021

@author: Ben
"""

import numpy as np

originalFish = np.loadtxt("Day6input.txt",delimiter=',')
#originalFish = np.array([3,4,3,1,2]) # Example input



runPart1 = False

if runPart1:
    numberOfDays = 80 #80

    currentFish = originalFish.copy()

    for day in range(numberOfDays):

        newFish = np.array([])
        for index, fish in enumerate(currentFish):
            if fish == 0:
                currentFish[index] = 6
                newFish = np.append(newFish,[8])
            else:
                currentFish[index] -= 1
        currentFish = np.append(currentFish,newFish)


    print("Number of fish = " + str(len(currentFish)))


# Way to slow and memory intensive to do it this way! Can't even run the example code. Instead, keep a total of the numbers

runPart2 = True

originalFish = list(originalFish)
numberOfDays = 256

currentFish = {
        0 : originalFish.count(0),
        1 : originalFish.count(1),
        2 : originalFish.count(2),
        3 : originalFish.count(3),
        4 : originalFish.count(4),
        5 : originalFish.count(5),
        6 : originalFish.count(6),
        7 : originalFish.count(7),
        8 : originalFish.count(8)
        }

newFish = {}

for day in range(numberOfDays):
    newFish = {
            0 : currentFish[1],
            1 : currentFish[2],
            2 : currentFish[3],
            3 : currentFish[4],
            4 : currentFish[5],
            5 : currentFish[6],
            6 : currentFish[7],
            7 : currentFish[8],
            8 : currentFish[0]
            }

    newFish[6] += currentFish[0]

    currentFish = newFish
    newFish = {}


total = 0

for fish in currentFish:
    total += currentFish[fish]

print("Total part 2 fish = " + str(total))

