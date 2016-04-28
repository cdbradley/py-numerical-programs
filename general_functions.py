#Colt Bradley
#General Functions

#import necessary modules
import numpy as np
import pylab as py

def RK2_2ndOrderODE(f,a0=0,b0=0,ti=0,tf=10,ts=100):
    a = a0
    b = b0
    dt = (tf-ti)/ts
    A = []
    B = []
    time = []
    t = 0
    
    for i in range(0, ts):
        #do first step
        a1 = a + b*dt/2
        b1 = b + f(a)*dt/2
        
        #do second step
        a = a + b1*dt
        b = b + f(a1)*dt
        
        #interate values and append solutions to a list
        t = t +dt
        return A.append(a)
        return B.append(b)
        return time.append(t)