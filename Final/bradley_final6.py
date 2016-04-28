#Colt Bradley
#4.28.16
#PY251 Final
#question6

#import modules
import numpy as np
import pylab as py

def central_difference(f,x,h):
    deriv = (f(float(x+h))-f(float(x-h)))/(2.*h)
    return deriv

def f(x):
    if x <1:
        r=2*x**3-1
    elif x>=1:
        r=np.sqrt(12*x-11)
    return r

x=np.linspace(0,2,num=11)
y=[]
for i in x:
    y.append(f(i))
 
deriv=[]
h = 0.01
for k in x:
    deriv.append(central_difference(f,k,h))
        
py.close()
py.plot(x,y)
py.plot(x,deriv)
py.show()

np.savetxt("question6.txt",zip(x,deriv))