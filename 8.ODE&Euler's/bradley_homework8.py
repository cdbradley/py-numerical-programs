#Colt Bradley
#2.4.16
#Homework 8

#import modules
import numpy as n
import pylab as p

#define variables from then homework
g = 9.8
y_0 = 12.
v_0 = 35.
t_0 = 0
t_f = 8.
nts = 1280
dt = (t_f - t_0)/nts

#create arrays
t = n.linspace(t_0, t_f,num = nts+1)
Y = n.zeros(len(t))
V = n.zeros(len(t))

#name the first elements of each array the initial value
Y[0] = y_0
V[0] = v_0

#creat the for loop that actually solves the equation. 
for i in range(0,nts):
    Y[i+1] = Y[i] + V[i]*dt
    V[i+1] = V[i] - g*dt

#Actual Value
t1 = v_0/g
y1 = -.5*g*t1**2 + v_0*t1 + y_0
t2 = 8-t1
y2 = (.5*g*t2**2)
actual = y1-y2
print actual #result of the above calculation
print Y[nts] #Result from iteration
error = (actual - Y[nts])/actual #calculated Error
print error

#build plot
p.plot(t,Y,"r")
p.plot(t,Y,"r.")
title = "Projectile height after {:.2f} seconds" .format(t_f)
p.xlabel("Time (seconds)", fontsize = 16)
p.ylabel("Height (meters)",fontsize = 16)
p.title(title)
p.show()
fig = "trial_{}" .format(nts) #Saves each plot with the number of time steps
p.savefig(fig+".png")

