##Colt Bradley
#3.15.2016
#Lesson 15

import os
os.chdir("C:/Users/Colt/OneDrive/Documents/Professional/School/16spring/PY_251/20.FourierAnalysis")

#############################################################################
#functions and modules
#############################################################################
#import modules
import numpy as n
import pylab as p

#define essential functions
#first is used in the first homeowrk exercise
def f(x):
    y = n.sin(6*n.pi*x)*n.exp(-x**2)
    return y
    
def ff(x,t):
    y = n.sin(6*n.pi*x)*n.exp(-x**2)*n.exp(-2*n.pi*1j*x*t)
    return y
    
def g(x):
    y = n.cos(6*n.pi*x)*n.exp(-x**2)
    return y
    
def a(x):
    y = n.sin(6*n.pi*3*x)*n.exp(-x**2)
    return y

def gf(x,t):
    y = n.cos(6*n.pi*x)*n.exp(-x**2)*n.exp(-2*n.pi*1j*x*t)
    return y

#fucntion simpson() is the simpson rule function
def simpsonfor(f,t,a,b,N):
    h = float(b-a)/N
    i = 1
    n = 1
    
    I_1 = 0.
    while i < N:
        I_1 += f(a+i*h,t)
        i += 1
    
    I_2 = 0   
    while n < N+1:
        I_2 += f(a+n*h - h/2,t)
        n += 1
    return (h/6)*(f(a,t)+f(b,t)+2*I_1+4*I_2)


#############################################################################
#Homework 3
#############################################################################
