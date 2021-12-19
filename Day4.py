# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 16:23:01 2021

@author: Ben
"""

import numpy as np
import pandas as pd

#inputs = np.loadtxt("Day4input.txt",delimiter=',')
#boards = pd.read_csv("Day4input.txt", sep='',skiprows=1)

with open('Day4input.txt') as f:
    # Getting the first line as the "bingo balls"
    bingo_balls = f.readline()
    
    # Getting the remaining lines as the "bingo boards"
    bingo_boards = f.readlines()
    
balls = np.array(bingo_balls.replace('\n','').split(','),dtype=int)

boards=[]
for board in bingo_boards:
    boards.append(list(map(int, board.replace('\n', '').split())))



boards = [board for board in boards if board != []]

# reformat into np 3d array

boards = np.reshape(boards, (-1,5,5))


#for ball in balls:
#    boards[np.where(boards == ball)]=0
#    sumX = np.sum(boards,axis=1)
#    sumY = np.sum(boards,axis=2)
#    
#    if len(np.where(sumX==0)[0]) != 0:
#        winnerNumbers = np.where(sumX==0)
#        print("Found X")
#        print(ball)
#        break
#    elif len(np.where(sumY==0)[0]) != 0:
#        winnerNumbers = np.where(sumY==0)
#        print("Found Y")
#        print(ball)
#        
#        break
#
#print("Winner sum:")
#print(np.sum(boards[winnerNumbers[0]]))
#print("Winner total:")
#print(np.sum(boards[winnerNumbers[0]])*ball)
#print(boards[winnerNumbers[0]])

# Part 2
boardsDummy = boards.copy()
boardsCopy = boards.copy()
for ball in balls:
    boardsDummy[np.where(boardsDummy == ball)]=0
    boardsCopy[np.where(boardsCopy == ball)]=0
    sumX = np.sum(boardsDummy,axis=1)
    sumY = np.sum(boardsDummy,axis=2)
    
    if len(np.where(sumX==0)[0]) != 0:
        winnerNumbers = np.where(sumX==0)
        print("Found X")
        winningBall= ball
        print(ball)
        boardsDummy[winnerNumbers[0],:,:] = 1000
        print(boardsCopy[winnerNumbers[0],:,:])
        winningBoard = boardsCopy[winnerNumbers[0],:,:]
        
    elif len(np.where(sumY==0)[0]) != 0:
        winnerNumbers = np.where(sumY==0)
        print("Found Y")
        print(ball)
        winningBall= ball
        boardsDummy[winnerNumbers[0],:,:] = 1000
        print(boardsCopy[winnerNumbers[0],:,:])
        winningBoard = boardsCopy[winnerNumbers[0],:,:]
        

print("Winner ball: " + str(winningBall))
print("Winner sum: " + str(np.sum(winningBoard)))
print("Winner total:")
print(np.sum(winningBoard)*winningBall)
print("Winning board")
print(winningBoard)

 