#Colt Bradley
#1.18.16
#working through lesson 3 ...plots

#import modules
import numpy as n
import math as m
import pylab as p

#parameters and input
t = n.linspace(0.,2.,100)
v0 = raw_input("Initial Velocity: ")
v0=float(v0)
g=9.8

#equation of interest
y = v0*t - .5*g*t**2

#Plot the function with a smooth curve through the data points
p.plot(t,y,"r")
#put a red dot where points are
p.plot(t,y,"r.")
#labels
p.title("Height of Object")
p.xlabel("Time (Seconds)", fontsize=16)
p.ylabel("height (meters)", fontsize=16)
p.show()