import pandas as pd
import math

error_trapezoidal = []
error_simpson_one_third = []

def function(t) : 
    mi = 140000
    q = 2100
    u = 2000
    return (u*math.log(mi/(mi-q*t))) - 9.8*t

def trapezoidal_rule(a,b,n) : 
    increment = (b-a)/n
    value = function(a) + function(b)
    for i in range(1,n,1) : 
        a = a + increment
        value = value + 2*function(a)
    value = value*(b-a)/2
    return value

def simpson_one_third(a,b,n) :
     increment = (b-a)/(2*n)
     value = function(a) + function(b) 
     for i in range(1,2*n,1) : 
         a = a + increment
         if(i % 2 == 0) : 
             value = value +2 * function(a)
         else :
             value = value +4 * function(a)
     value = value*(b-a)/3
     return value
 

disTrap = []
disSimp = []

for i in range(0,5,1) : 
    disTrap.append(trapezoidal_rule(8, 30, i+1))
    disSimp.append(simpson_one_third(8, 30, i+1))
    if(i != 0) : 
        error_simpson_one_third.append(abs((disSimp[i]-disSimp[i-1])/disSimp[i-1]))
        error_trapezoidal.append(abs((disTrap[i]-disTrap[i-1])/disTrap[i-1]))

disTableTrap = pd.DataFrame(disTrap,columns=['Distance'])
errorTableTrap = pd.DataFrame(error_trapezoidal,columns=['Absolute Relative approx. Error'])
disTableSimp = pd.DataFrame(disSimp,columns=['Distance'])
errorTableSimp = pd.DataFrame(error_simpson_one_third,columns=['Absolute Relative approx. Error'])



print('Data Table for Trapezoidal Rule: ')
print(disTableTrap)
print(errorTableTrap)
print('Data Table for Simpson 1/3rd Rule: ')
print(disTableSimp)
print(errorTableSimp)
print('Enter number of Segment: ')
n = int(input())
print('Calculated Value by Trapezoidal Rule')
print(trapezoidal_rule(8, 30, n))
print('Calculated Value for Simpson 1/3rd rule')
print(simpson_one_third(8, 30, n))