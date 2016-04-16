#Colt Bradley
#1.14.16
#working through lesson 3

#import math as m
#can also use "from math import *" But this can cause some issues
import math as m
#now we import numpy as well
import numpy as n


#Ask user for initial velocity, vertical position, then convert to floats
v0 = raw_input('Initial Velocity: ')
v0 = float(v0)
y = raw_input('Verticle Position: ')
y = float(y)
g = 9.8

#calculate value
t_plus = (v0 + m.sqrt(v0**2 - 2*g*y))/g
t_minus = (v0 + m.sqrt(v0**2 - 2*g*y))/g

print "The plus value is {}, the minus value is {}" .format(t_plus, t_minus)