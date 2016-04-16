#Colt Bradley
#1.18.16
#Working through lesson 3....Arrays

#import math, numpy (for linspace)
import math as m
import numpy as n

#create list, five elements 
##linspace(a,b,s) creates list with s elements between a, b. Always real numbers
t1=n.linspace(1.,3.,5)
#creates a list of the numbers you type
t2=n.array([1., 1.5, 2., 2.5, 3.])
#arange: similar to linspace, but incriments to less than b. 
t3=n.arange(1,3.1,.5)
#arange can have issues, for example
t4=n.arange(2,7,1)
t5=n.arange(15.1,18.1,.3)


print t1
print t2
print t3
print t4
print t5

#experiment with our lists
#inditial data and parameters
t = n.linspace(1.,3.,5)
v0=raw_input("Initial Velocity: ")
v0=float(v0)
g=9.8

#compute the heights for the array of times t
y = v0*t-.5*g*t**2

print "The heights at times t = {} are y = {}" .format(t,y)