import random
import matplotlib.pyplot as plt
import numpy as np
#packages
def randomPoints(x,y,w,z,n):
    l = []
    for i in range(n):
        x1 = x
        y1 = y
        w1 = w
        z1 = z
#sets up variables
        t = random.randint(0,101)/100
        x1 *= t
        y1 *= t
        w1 *= (1-t)
        z1 *= (1-t)
        u = x1+w1
        v = y1+z1
        u = round(u,2)
        v = round(v,2)
        l.append([u,v])
        
    return l
#generates a number between 0 and 1, plugs number into x,y,w,z
def xVal(pairs):
    xVals = []
    for x in pairs:
        xVals.append(x[0])
    return xVals
#gets all x values in the list
def yVal(pairs):
    yVals = []
    for x in pairs:
        yVals.append(x[1])
    return yVals
#gets all y values in the list
points = randomPoints(3,2,9,6,200)
points2Electricboogaloo = randomPoints(4,7,1,8,200)
# depict illustration
plt.scatter(xVal(points), yVal(points))
plt.scatter(xVal(points2Electricboogaloo),yVal(points2Electricboogaloo))
 
# apply legend()
plt.legend(["set1" , "set2"])
plt.show()