#Colt Bradley
#1.19.16
#Lesson 4 Homework

#import modules 
import numpy as n

#Question 1
x = n.arange(-2,12,2)
print x

#Question 2
a = [19,4,-7,13,55,-12,16,8]
print a[3]
print a[3:]
print a[:3]

#question 3
x = 5**3
print type(x)
x = 5.**3
print type(x)
x = 5**3.
print type(x)

#question 4
x = 7
y = 4.2
print type(x)
print type(y)
print type(x+y)
print type(x*y)

#Question 5
x = 3.4
y = 2+8j
print type(x)
print type(y)
print type(x+y)
print type(x*y)

#Question 6
x=10./3.
print "x = {:.2f}".format(x)

#Question 7
#prompt user for first and last name
name1,name2 = raw_input("What\'s your first and last name? ").split()

#grab the initials and string combine them
initials = name1[0]+name2[0]

#print necessary info
print "Hello {} {}. Your initials are {}" .format(name1,name2,initials)

#now ask for an intial hgiht and velocity of a 1-d particle in gravity
y0 = raw_input("What's the height of a projectile? ")
y0 = float(y0)
v0 = raw_input("What's the initial velocity of that projectile?")
v0 = float(v0)

#essential values
g = 9.8


#preform calculation
t1 = v0/g
y1 = -.5*g*t1**2 + v0*t1
t2 = n.sqrt(2*(y1+y0)/g)
time = t1 + t2

#print total flight time
print "The total time of flight for the object is t = {:.3f} s." .format(time)