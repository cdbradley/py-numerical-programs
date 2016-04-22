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
A = 0.1
sigma = 1.0

# Set up grid
N = 100  # number of space intervals
nts = 200  # number of timesteps
plt = 20 # number of timesteps between plots
dx = (xb - xa)/N
dt = 0.25*dx/c
cdtoverdxsqr = (c*dt/dx)**2
x = np.linspace(xa,xb,N+1)

# arrays
y = np.zeros(N+1)
ym = np.zeros(N+1) # "y_minus" = y at previous timestep
yp = np.zeros(N+1) # "y_plus"  = y at next timestep

# initial data
for i in range(0,N+1,1):
    ym[i] = A*np.exp(-(x[i]/sigma)**2)
pl.close()
pl.plot(x,ym)

# take the first timestep
y = np.copy(ym)
n = 1
time = dt

# Evolve
while n < nts:
    for i in range(1,N,1):
        yp[i] = 2.0*y[i] - ym[i] + cdtoverdxsqr*(y[i+1] - 2.0*y[i] + y[i-1])
    ym = np.copy(y)
    y = np.copy(yp)
    n = n + 1
    time = time + dt
    if (plt*(n/plt) == n): #plot every plt timesteps
        pl.plot(x,y)
        print n, time

pl.title("Amplitude of Gaussian pulse at various times 1")
pl.xlabel('x')
pl.ylabel('y')
pl.savefig("part1.png")
pl.show()
