#Colt Bradley
#1.26.16
#Working through lesson 5 part 2

#import packages
import numpy as n
import pylab as p

#exercise 4
integer = raw_input("Give me an integer ")
integer = int(integer)

i = 1
for i in range (1,10,1):
    if i == integer:
        print "Done"
        break
    else:
        print "{} and..." .format(i)
        i = i+1
        
#Exercise 5
import numpy as n
v0 = 100.0 # initial velocity [m/s]
y0 = 1.0 # initial position [s]
g = 9.80 # acceleration [m/s^2]
t = n.linspace(0.0,100.0,1001) # array of times in 0.1 s increments
y = n.zeros(len(t)) # array of zeros, same length as t

# find positions y[i] at times t[i]
for i in range(len(t)):
    y[i] = y0 + v0*t[i] - 0.5*g*t[i]**2
    
p.plot(t,y,"r")
p.show()