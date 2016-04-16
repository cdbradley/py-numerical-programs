#Colt Bradley
#2.25.16
#Homework 12

#import modules
import numpy as n

#define variables
m = 14
l = 1.2
g = 9.8
theta = 35

#Define the matricies
big = n.matrix([[1, 0 ,-n.cos(theta)],[0,1,n.sin(theta)],\
[0, -l/2., n.sin(theta)*l/2]])
col = n.matrix([[0],[m*g],[0]])

#use linear algebra package, print result
print n.linalg.solve(big,col)

############################################################################
#Part 2
############################################################################

#define variables, emf in Volts and r in ohms
emf_1 = 12
emf_2 = 9
r_1 = 100
r_2 = 130
r_3 = 65

#define matricies
res = n.matrix([[r_1,0,r_3],[0,r_2,r_3],[1,1,-1]])
emfs = n.matrix([[emf_1],[emf_2],[0]])

#use linear algebra package, print result
print n.linalg.solve(res,emfs)