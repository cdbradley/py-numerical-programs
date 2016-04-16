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
N = []
R = []


t=n.linspace(0,30,128000)
dt = t[1]-t[0]
u = -n.pi/2
v = 0.
g = 1.25
w = n.pi*2
w0 = 1.5*w
b = w0/4.
U = []
V = []
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
        
    V.append(v)
    U.append(u)
N.append(V[-1])

p.close()
p.plot(time,U,"r")
p.title("Gamma = 1.25")
p.xlabel("Time (periods)")
p.ylabel("Angle (radians)")
p.savefig("g25theta.png")
p.show()

p.close()
p.plot(V,U,"r")
p.title("Gamma = 1.25")
p.xlabel("Psy")
p.ylabel("Angle (radians)")
p.savefig("g25psy.png")
p.show()