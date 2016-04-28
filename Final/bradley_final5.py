#Colt Bradley
#4.28.16
#PY251 Final
#question5

#import modules
import numpy as np
import pylab as py

def f(x,t):
    return x*t
def g(x,y):
    return y**2-x
    
#Initial Values and Setup    
time = []
N = []
R = []


t=np.linspace(0,2,100000)
dt = t[1]-t[0]
x = 1.
y = 0.
X = []
Y = []
for i in range (0,len(t)-1):
    ti = t[i]
    th = ti +dt/2.
    tf = t[i+1]
    time.append(ti)
    
    xa = x +f(x,ti)*dt/2.
    ya = y +g(x,y)*dt/2.
    
    xb = x +f(xa,th)*dt/2.
    yb = y +g(xa,ya)*dt/2.
    
    xc = x +f(xb,th)*dt
    yc = y +g(xb,yb)*dt
    
    xd = x +f(xc,tf)*dt
    yd = y +g(xc,yc)*dt
     
    x = (xa+2*xb+xc+(xd/2.))/3-x/2
    y = (ya+2*yb+yc+(yd/2.))/3-y/2
        
    X.append(x)
    Y.append(y)

py.close()
py.plot(time,X,"r")
py.plot(time,Y,"b")
py.title("Function values for X, Y")
py.xlabel("Function Values")
py.ylabel("Time(s)")
py.savefig("final5.png")
py.show()