#Colt Bradley
#2.9.16
#Lesson 9

#import numpy, pylab
import numpy as n
import pylab as p

n0 = 100
tau = 5.
tf = 10.
ts = 10000
dt = tf/ts

for i in range(0,ts):
    n0 = n0 - n0*dt/tau
    
print n0
print abs((13.5335-n0)/13.5335)*100

