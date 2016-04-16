#Colt Bradley
#1.18.16
#Homework for Lesson 3

#Import modules numpy for mathy stuff and pylab for plots
import numpy as n
import pylab as p

#Ask user for initial velocity and theta
v0 = raw_input("Initial Velocity: ")
v0 = float(v0)
theta = raw_input("Initial Angle: ")
theta = float(theta)

#Import parameters and convert user-given values
theta = n.pi*theta/180
vy = v0*n.sin(theta)
vx = v0*n.cos(theta)
g = 9.8
t = n.linspace(0.,3.,100)

#Essential equations
x = vx*t
y = vy*t - .5*g*t**2

#plot commands
p.plot(x,y,"r")
p.plot(x,y,"r.")
#plot labels
p.title("xy position of object")
p.xlabel("x position of object (Meters)",fontsize=16)
p.ylabel("y position of object (meters)",fontsize=16)
p.show()
p.savefig("xy_projectile.png")
