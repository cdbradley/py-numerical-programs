#Colt Bradley
#Lesson 18
#4.5.16

#import essential modules
import numpy as n
import pylab as p

def f(u,v,t):
    g = 1.25
    w = n.pi*2
    w0 = 1.5*w
    b = w0/4.
    return -w0**2*n.sin(u)-2*b*v+g*w0**2*n.cos(w*t)
    
#Initial Values and Setup    
time = []
N1 = []
N2 = []



t=n.linspace(0,15,128000)
dt = t[1]-t[0]
u = -n.pi/2
v = 0.
g = 1.25
w = n.pi*2
w0 = 1.5*w
b = w0/4.
U1 = []
U2 = []
V1 = []
V2 = []
for i in range (0,len(t)-1):
    ti = t[i]
    th = ti +dt/2.
    tf = t[i+1]
    time.append(ti)
    
    va = v +u*dt/2.
    ua = u +f(v,u,ti)*dt/2.
    vb = v +ua*dt/2.
    ub = u +f(va,ua,th)*dt/2.
    vc = v +ub*dt
    uc = u +f(vb,ub,th)*dt
    vd = v +uc*dt
    ud = u +f(vc,uc,tf)*dt
     
    v = (va+2*vb+vc+(vd/2.))/3-v/2
    u = (ua+2*ub+uc+(ud/2.))/3-u/2
        
    V1.append(v)
    U1.append(u)
N1.append(V1[-1])

u = -n.pi/2+.0001
for i in range (0,len(t)-1):
    ti = t[i]
    th = ti +dt/2.
    tf = t[i+1]
    
    va = v +u*dt/2.
    ua = u +f(v,u,ti)*dt/2.
    vb = v +ua*dt/2.
    ub = u +f(va,ua,th)*dt/2.
    vc = v +ub*dt
    uc = u +f(vb,ub,th)*dt
    vd = v +uc*dt
    ud = u +f(vc,uc,tf)*dt
     
    v = (va+2*vb+vc+(vd/2.))/3-v/2
    u = (ua+2*ub+uc+(ud/2.))/3-u/2
        
    V2.append(v)
    U2.append(u)
N2.append(V2[-1])

delta = n.zeros(len(U1))

for k in range(len(U1)):
    delta[k] = abs(U1[k]-U2[k])

p.close()
p.plot(time,delta,"r")
p.title("Angle difference with different initial conditions - Chaotic")
p.xlabel("Time (periods)")
p.ylabel("Absolute value of  the difference in Angle")
p.savefig("deltathetachaos.png")
p.show()

