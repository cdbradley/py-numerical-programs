#Colt Bradley
#4.18.16
#Lesson 21: Boundry Value Problems

###############################################################################
#Import Modules and define functions
###############################################################################
import numpy as np
import pylab as py

###############################################################################
#Part 1
###############################################################################

#define values
k=5.
f_0=0.
f_f=2.
N=100
change = 10.
ch=[]
steps=0
h = (f_f-f_0)/N
X=np.linspace(0,1,100)
Y=np.zeros(N)
Y[0]=f_0
Y[-1]=f_f
for i in range(len(Y+1))[1:-1]:
    Y[i]=Y[i-1]+h
ch.append(Y[50])

while change>.00000000001:    
    Y[1:-1] = .5*(Y[:-2]+Y[2:])-(k*h**2)/2.*np.sqrt(1+((Y[:-2]-Y[2:])**2)/(2*h)**2)
    ch.append(Y[50])
    change = abs(ch[-1]-ch[-2])
    steps=+1

print steps

py.close()
py.plot(X,Y,"b")
py.show()