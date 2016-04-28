#Colt Bradley
#4.28.16
#PY251 Final
#question5

#import modules
import numpy as np
import pylab as py

    
#Initial Values and Setup    
time = []
N = []
R = []


t=np.linspace(0,2,60000)
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
    
    xa = x +u*dt/2.
    ua = u +f(v,u,ti)*dt/2.
    
    vb = v +ua*dt/2.
    ub = u +f(va,ua,th)*dt/2.
    
    vc = v +ub*dt
    uc = u +f(vb,ub,th)*dt
    
    vd = v +uc*dt
    ud = u +f(vc,uc,tf)*dt
     
    x = (xa+2*xb+xc+(xd/2.))/3-x/2
    u = (ya+2*yb+yc+(yd/2.))/3-y/2
        
    X.append(x)
    Y.append(y)

py.close()
py.plot(time,X,"r")
py.plot(time,Y,"b")
py.title("Function values for X, Y")
py.xlabel("Time (periods)")
py.ylabel("Time(s)")
py.savefig("final5.png")
py.show()