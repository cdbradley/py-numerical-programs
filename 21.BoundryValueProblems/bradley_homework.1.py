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
x_0=0.
x_f=1.
y_0=0.
y_f=2.
N=100.
change = 10.
ch=[]
steps=0
h = (x_f-x_0)/N
X=np.linspace(0,1,100)
#build list of y values
Y=np.zeros(N)
Y[0]=y_0
Y[-1]=y_f
for i in range(len(Y+1))[1:-1]:
    Y[i]=Y[i-1]+h
ch.append(Y[50])

#set the loop to happen while outside a certain error tolerance
while change>.00001:    
    Y[1:-1] = .5*(Y[:-2]+Y[2:])-(k*h**2)/2.*np.sqrt(1+((Y[:-2]-Y[2:])**2)/(2*h)**2)
    ch.append(Y[50])
    change = abs(ch[-1]-ch[-2])
    steps= steps+1

#print number of sweeps required for the code to run
print steps

py.close()
py.plot(X,Y,"b")
py.title("String relaxation with .0000001 error allowed")
py.xlabel("X-Distance (m)",fontsize = 16)
py.ylabel("Y-Distance (m)",fontsize = 16)
py.savefig("1_relaxation(.0000001).png")
py.show()
