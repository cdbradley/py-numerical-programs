#Colt Bradley
#4.18.16
#Lesson 21: Boundry Value Problems

###############################################################################
#Import Modules and define functions
###############################################################################
import numpy as np
import pylab as py

###############################################################################
#Part 2
###############################################################################
#Colt Bradley
#4.18.16
#Lesson 21: Boundry Value Problems

###############################################################################
#Import Modules and define functions
###############################################################################
import numpy as np
import pylab as py

def L_1(N,Y):
    sum=0
    for i in range(N+1)[1:-1]:
        sum = sum + (Y[i]-Y[i-1])**2
    return (1./N)*sum

###############################################################################
#Part 1
###############################################################################

#define values
k=5.
x_0=0.
x_f=1.
y_0=0.
y_f=2.
N=100
L = 10.
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
#we'll look at the error tolerance half way through the chain
while L>.000847:    
    Y[1:-1] = .5*(Y[:-2]+Y[2:])-(k*h**2)/2.*np.sqrt(1+((Y[:-2]-Y[2:])**2)/(2*h)**2)
    ch.append(Y[N/2])
    L = L_1(N,Y)
    steps= steps+1

#print number of sweeps required for the code to run
print steps

py.close()
py.plot(X,Y,"b")
py.title("String relaxation while L norm is less than .000847")
py.xlabel("X-Distance (m)",fontsize = 16)
py.ylabel("Y-Distance (m)",fontsize = 16)
py.savefig("2_relaxationWithL.png")
py.show()