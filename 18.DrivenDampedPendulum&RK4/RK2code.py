# RK2 integration of x' = sin(10*t*x)
import numpy as n
import pylab as p

# define the right-hand side
def rhs(x,t): 
    return n.sin(10*t*x)

# initial/final times, timestep
t0 = 0.0
tf = 100.0
nts = 1000
dt = (tf - t0)/nts
dth = 0.5*dt

# set up arrays and initial conditions
t = n.linspace(t0, tf, nts+1)
x = n.zeros(len(t))
x[0] = 1.0

# Main loop. Step forward in time with RK2
for i in range(0,nts):
    xh = x[i] + rhs(x[i],t[i])*dth
    th = t[i] + dth
    x[i+1] = x[i] + rhs(xh,th)*dt

# print/plot results
print t[nts], x[nts]
#p.close()
#p.plot(t,x,'b.')
#p.show()
