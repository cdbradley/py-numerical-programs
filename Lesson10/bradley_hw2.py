import numpy as n
import pylab as p

#define Values
m = .00104
D = .00559
v0 = 500.
rho = 1.28
mu = .0000183

r_e1 = rho*v0*D/mu
print r_e1
print r_e1<10**6

#RK2 method
#define values, using some of above values
v = v0
y0 = 0
y = y0
g = 9.8
A = ((D/2)**2)*n.pi
tf = 20.
ts = 10000
dt = tf/ts
Y = []
V = []
time = []
t = 0

for i in range(0, ts):
    #define reynolds number, drag coefficient for first step
    r_e2 = rho*abs(v)*D/mu
    c_d1 = (24/r_e2)+((2.6*(r_e2/5.))/(1+(r_e2/5.)**1.52))+((.411*(r_e2/263000)**(-7.94))/(1+(r_e2/263000)**(-8.)))+(r_e2**(.8)/461000.)
    
    #do first step
    y1 = y + v*dt/2
    v1 = v + (-g - ((rho*A*abs(v)*c_d1*v)/(2*m)))*dt/2
    
    #define reynolds number, drag coefficent for second step
    r_e3 = rho*abs(v1)*D/mu
    c_d2 = (24/r_e3)+((2.6*(r_e3/5.))/(1+(r_e3/5.)**1.52))+((.411*(r_e3/263000)**(-7.94))/(1+(r_e3/263000)**(-8.)))+(r_e3**(.8)/461000.)
    
    #do second step
    y = y + v1*dt
    v = v + (-g - ((rho*A*abs(v1)*c_d2*v1)/(2*m)))*dt
    
    #interate values and append solutions to a list
    t = t +dt
    V.append(v)
    Y.append(y)
    time.append(t)
    
#create and save plot for the height
p.close()
p.plot(time,Y,"r")
p.title("Particle Height vs Time")
p.ylabel("Particle Height (m)", fontsize = 16)
p.xlabel("Time (s)",fontsize = 16)
p.show()
p.savefig("heightplot.png")

#create and save plot for velocity
p.close()
p.plot(time,V,0,"r")
p.title("Particle Velocity vs Time")
p.ylabel("Particle Velocity (m/2)", fontsize = 16)
p.xlabel("Time (s)",fontsize = 16)
p.show()
p.savefig("velocityplot.png")