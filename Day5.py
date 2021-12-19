# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 15:43:25 2021

@author: Ben
"""
import numpy as np

with open('Day5input.txt') as f:
    ventLinesRaw = f.readlines()

ventLines = np.array([list(map(int, vents.replace('->', ',').split(','))) for vents in ventLinesRaw])


minn = np.min(ventLines,axis=0)
xmin = np.min([minn[0],minn[2]])
ymin = np.min([minn[1],minn[3]])

maxx = np.max(ventLines,axis=0)
xmax = np.max([maxx[0],maxx[2]])
ymax = np.max([maxx[1],maxx[3]])

# part 1
seaFloor = np.zeros([xmax+1,ymax+1])

for line in ventLines:
    if line[0]-line[2] == 0:
        ysmall = np.min([line[1],line[3]])
        ybig = np.max([line[1],line[3]])+1
        seaFloor[line[0],ysmall:ybig] += 1
    elif line[1]-line[3] == 0:
        xsmall = np.min([line[0],line[2]])
        xbig = np.max([line[0],line[2]])+1
        seaFloor[xsmall:xbig,line[1]] += 1
    else:
        print("Not vertical or horizontal")
dangerZone = seaFloor>1                
print("Vent lines more than 2")
print(dangerZone.sum())


# part 2
seaFloor = np.zeros([xmax+1,ymax+1])

for line in ventLines:
    if line[0]-line[2] == 0:
        ysmall = np.min([line[1],line[3]])
        ybig = np.max([line[1],line[3]])+1
        seaFloor[line[0],ysmall:ybig] += 1
    elif line[1]-line[3] == 0:
        xsmall = np.min([line[0],line[2]])
        xbig = np.max([line[0],line[2]])+1
        seaFloor[xsmall:xbig,line[1]] += 1
    else:
        if line[0]>line[2]:
            xrange = np.arange(line[0],line[2]-1,-1)
        elif line[0]<line[2]:
            xrange = np.arange(line[0],line[2]+1,1)
        if line[1]>line[3]:
            yrange = np.arange(line[1],line[3]-1,-1)
        elif line[1]<line[3]:
            yrange = np.arange(line[1],line[3]+1,1)
        
        for index, x in enumerate(xrange):
            seaFloor[x,yrange[index]] +=1
            
        
        
dangerZone = seaFloor>1                
print("Part2: Vent lines more than 2")
print(dangerZone.sum())
#
#
#ysmall = np.min([line[1],line[3]])
#        ybig = np.max([line[1],line[3]])+1
#        xsmall = np.min([line[0],line[2]])
#        xbig = np.max([line[0],line[2]])+1