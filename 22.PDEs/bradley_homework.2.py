#Colt Bradley
#4.21.16
#PDEs
# Solve the PDE for waves on a string
import pylab as pl
import numpy as np

# Parameters
c = 50.0
xa = -5.0
xb = 5.0
A = .1
sigma = 1.

# Set up grid
N = 100  # number of space intervals
nts = 200  # number of timesteps
plt = 20 # number of timesteps between plots
dx = (xb - xa)/N
dt = 0.25*dx/c
x = np.linspace(xa,xb,N)

# arrays
y = np.zeros(N)
ym = np.zeros(N) # "y_minus" = y at previous timestep
yp = np.zeros(N) # "y_plus"  = y at next timestep
v = np.zeros(N)
vm = np.zeros(N) # "v_minus" = v at previous timestep
vp = np.zeros(N) # "v_plus"  = v at next timestep

# initial data
for i in range(0,N,1):
    y[i] = A*np.exp(-(x[i]/sigma)**2)
pl.close()
pl.plot(x,y)

# take the first timestep
ym = np.copy(y)
n = 1
time = 0

#populate initial arrays

# Evolve
while n < nts:
    #first step
    ym[:] = y[:] +(dt/2.)*v[:]
    vm[1:-1] = v[1:-1] +(dt/2.)*(c**2.)*((y[2:]-2.*y[1:-1]+y[:-2])/dx**2.)
    #second step
    yp[:] = y[:]+dt*vm[:]
    vp[1:-1] = v[1:-1] +(dt)*(c**2.)*((ym[2:]-2.*ym[1:-1]+ym[:-2])/dx**2.)
    
    v = np.copy(vp)
    y = np.copy(yp)
    n = n + 1
    time = time + dt
    if (plt*(n/plt) == n): #plot every plt timesteps
        pl.plot(x,yp)
        print n, time
       
pl.title("Amplitude of Gaussian pulse at various times 2")
pl.xlabel('x')
pl.ylabel('y')
pl.savefig("part2.png")
pl.show()
