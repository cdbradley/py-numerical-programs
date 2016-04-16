#Colt Bradley
#2.25.16
#Lesson 12

#import modules
import numpy as n

coef = n.matrix([[2,5,-1],[-1,3,4],[4,0,-6]])
coefin = n.linalg.inv(coef)
r = n.matrix([[-8.5],[3],[-10]])
v = coefin*r
print v

print n.linalg.solve(coef,r)