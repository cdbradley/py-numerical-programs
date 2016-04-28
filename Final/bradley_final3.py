#Colt Bradley
#4.28.16
#PY251 Final
#question3

#import modules
import numpy as np
import pylab as py

#fucntion simpson() is the simpson rule function
def simpson(f,a,b,N):
    h = float(b-a)/N
    i = 1
    n = 1
    
    I_1 = 0.
    while i < N:
        I_1 += f(a+i*h)
        i += 1
    
    I_2 = 0   
    while n < N+1:
        I_2 += f(a+n*h - h/2)
        n += 1
    return (h/6)*(f(a)+f(b)+2*I_1+4*I_2)

#define function to integrate    
def f(x):
    y=np.sqrt(x)*np.sin(x)
    return y
    
a=0
b=6*np.pi
print simpson(f,a,b,5)
print simpson(f,a,b,10)
print simpson(f,a,b,15)
print
print "Result of interest:"
print simpson(f,a,b,20)
print
print simpson(f,a,b,25)
print simpson(f,a,b,30)
print simpson(f,a,b,35)
print
print simpson(f,a,b,1000)

# we look at the results surrounding 20 times steps, and see that -3.71 is consistant, so we belive that. 
#This also matches when we take a large number of steps, as seen in the final calculation

    