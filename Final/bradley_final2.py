#Colt Bradley
#4.28.16
#PY251 Final
#question2

#import modules
import numpy as np
import pylab as py

#Use linear algebra
A= np.matrix([[1,-2,5],[-3,1,-4],[2,0,-7]])
r = np.matrix([[-5],[7],[2]])

print np.linalg.solve(A,r)

#Answer:
#[[-1.3902439 ]
 #[ 0.09756098]
# [-0.68292683]]
