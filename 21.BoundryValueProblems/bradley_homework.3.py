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

#fucntion simpson() is the simpson rule function
def simpson(f,a,b,N):
    h = float(b-a)/N
    i = 1
    n = 1
    
    I_1 = 0.
    while i < N:
        I_1 += f(a+i*h)
        i += 1
    
    I_2 = 0   
    while n < N+1:
        I_2 += f(a+n*h - h/2)
        n += 1
    return (h/6)*(f(a)+f(b)+2*I_1+4*I_2)
###############################################################################
#Part 3
###############################################################################

#define values
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
R=[]

#set the loop to happen while outside a certain error tolerance
#we'll look at the error tolerance half way through the chain
#we use the open form for the integral
for k in [1.,2.,3.,4.,5.,6.,7.,8.]:
    ch=[]
    for i in range(len(Y+1))[1:-1]:
        Y[i]=Y[i-1]+h
    ch.append(Y[50])
    change = 10    
    while change>.00001:    
        Y[1:-1] = .5*(Y[:-2]+Y[2:])-(k*h**2)/2.*np.sqrt(1+((Y[:-2]-Y[2:])**2)/(2*h)**2)
        ch.append(Y[50])
        change = abs(ch[-1]-ch[-2])
        steps= steps+1
    F=[]
    I=0
    for i in range(100)[1:-1]:
        F.append(np.sqrt(1+((Y[i+1]-Y[i-1])/2*h)**2)*h)
    for k in F[1:-1]:
        I=I+k
    I = I+(3/2)*F[0]+(3/2)*F[-1]
    R.append(I)

py.close()
py.plot([1.,2.,3.,4.,5.,6.,7.,8.],R,"b.")
py.title("Length of string vs K value")
py.xlabel("K-vlaue",fontsize = 16)
py.ylabel("Length (m)",fontsize = 16)
py.savefig("3_LvK.png")
py.show()