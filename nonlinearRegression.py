import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sympy import *

def plotFunction(x_coord, y_coord):
    plt.plot(x_coord,y_coord)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    
def evaluateFunction(x_interp, dividedDif, x, n): 
    value = []
    error = []
    value.append(dividedDif[0][0])
    xTerm = 1
    for i in range(1,n,1): 
        xTerm = xTerm*(x_interp-x[i-1])
        value.append(value[i-1] + dividedDif[i][0]*xTerm)
        error.append(value[i]-value[i-1])
    
    return value[n-1],error

def NewtonDividedDifPolynom(x, y , n, x_interp):
    dividedDif = [[0 for i in range(n)] for j in range(n)]
    
    #calculate DividedDifference
    for i in range(0,n,1): 
        dividedDif[0][i] = y[i]
    
    for i in range(1,n,1):
        for j in range(0,n-i,1): 
            dividedDif[i][j] = (dividedDif[i-1][j+1]-dividedDif[i-1][j]) / (x[i+j] - x[j])

    #calculate polynomial
    val, error = evaluateFunction(x_interp, dividedDif, x, n)
    
    #plotting Curve
    toPlotX = np.arange(19,31,0.1)
    
    y = []
    for k in toPlotX:
        v, e = evaluateFunction(k, dividedDif, x, n)
        y.append(v)
    
    toPlotY = np.array(y)
    plotFunction(toPlotX, toPlotY)
    
    y2, e = evaluateFunction(x_interp+0.01, dividedDif, x, n)
    y1, e = evaluateFunction(x_interp-0.01, dividedDif, x, n)
    
    derivative = (y2-y1)/0.02
    
    return val, error, derivative

def takeInput(): 
    n = int(input())
    for i in range(0,n,1):
        a, b = [float(s) for s in input().split()]
        x.append(a)
        y.append(b)
    print('point to Interpolate:')
    x_interp = float(input())
    closeX, closeY = selectClosestPoint(n, x_interp, 5)
    val, error, der = NewtonDividedDifPolynom(closeX, closeY, 5, x_interp)
    
    errorTable = pd.DataFrame(error, columns=['Relative Approx Error'])
    print(errorTable)
    print('The interpolated value: ')
    print(val)
    print('Approx. Net Force: (in Newton)')
    print(der*1000)
    
def selectClosestPoint(n, x_interp, order): 
    closestX = []
    closestY = []
    taken = [0 for i in range(n)]
    
    for i in range(0,order,1):
        idx = -1
        mn = 99999999
        for j in range(0,n,1):
            if(taken[j] == 0 and abs(x_interp-x[j]) <= mn):
                mn = abs(x_interp-x[j])
                idx = j
        if(idx != -1):
            taken[idx] = 1
            closestX.append(x[idx])
            closestY.append(y[idx])
    
    return closestX, closestY
        
 
x = []
y = []
print('input for Mass: ')
takeInput()
x = []
y = []
print('input for velocity')
takeInput()



    
    
    
    