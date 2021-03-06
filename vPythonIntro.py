#!/usr/bin/env python3
from vpython import *
from time import *

mRadius= 2
wallThickness = 1
roomWidth = 15
roomDepth = 12
roomHeight = 8

floor = box(pos = vector(0, -roomHeight/2, 0), size = vector(roomWidth, wallThickness, roomDepth), color = color.white)
ceiling = box(pos = vector(0, roomHeight/2, 0), size = vector(roomWidth, wallThickness, roomDepth), color = color.white)
rightWall = box(pos = vector(roomWidth/2, 0, 0), size = vector(wallThickness, roomHeight, roomDepth), color = color.white)
leftWall = box(pos = vector(-roomWidth/2, 0, 0), size = vector(wallThickness, roomHeight, roomDepth), color = color.white)
backWall = box(pos = vector(0, 0, -roomDepth/2), size = vector(roomWidth, roomHeight, wallThickness), color = color.white)
marble = sphere(color = color.red, radius = mRadius)

deltaX = .1
xPos = 0

while True:
    rate(50)
    xPos= xPos + deltaX
    mRight = xPos + mRadius
    mLeft = xPos - mRadius
    rightWallEdge = roomWidth/2 - wallThickness/2
    leftWallEdge = -roomWidth/2 + wallThickness/2
    if mRight >= rightWallEdge or mLeft <= leftWallEdge:
        deltaX = deltaX * (-1)
    marble.pos=vector(xPos, 0, 0)