#Colt Bradley
#2.9.16
#Homework 9

#import numpy and pylab
import numpy as n
import pylab as p

###################################################
#Exercise 1
###################################################

#define values
n0 = 100
tau = 5.
tf = 10.
ts = 100
dt = tf/ts
i = 0.
data = []
error = []
nts = []

#for Loop
while ts < 10000000000: 
    n0 = 100
    i=0
    dt = tf/ts  
    while i < ts: 
        n0 = n0 - n0*dt/tau
        i = i+1
    nts.append(ts)
    ts = ts*10
    err = (13.5335-n0)/13.5335*100
    err = abs(err) 
    data.append(n0)
    error.append(err)

#write answer to file
n.savetxt("eulerdata.txt", zip(nts,data,error))

#read back the data, plot in Log plot
X,Y = n.loadtxt("eulerdata.txt",usecols = (0,2), unpack = True)
X = n.log10(X)
Y = n.log10(Y)
p.close()
p.plot(X,Y,"r")
p.plot(X,Y,"r.")
p.title("log(Error) vs. log(nts) using Euler")
p.xlabel("log(nts)",fontsize=16)
p.ylabel("log(Error)", fontsize=16)
p.show()
p.savefig("eulererrorplot.png")

#################################################
#################################################]
#Exercise 2
#################################################

#define values
n0 = 100
tau = 5.
tf = 10.
ts = 10
dt = tf/ts
i = 0.
data = []
error = []
nts = []

#for Loop
while ts < 10000000000: 
    n0 = 100
    i=0
    dt = tf/ts  
    while i < ts: 
        n1 = n0 - n0*dt/2/tau
        n0 = n0 - n1*dt/tau
        i = i+1
    nts.append(ts)
    ts = ts*10
    err = (13.5335-n0)/13.5335*100
    err = abs(err) 
    data.append(n0)
    error.append(err)

#write answer to file
n.savetxt("rkdata.txt", zip(nts,data,error))

#read back the data, plot in Log plot
X,Y = n.loadtxt("rkdata.txt",usecols = (0,2), unpack = True)
X = n.log10(X)
Y = n.log10(Y)
p.close()
p.plot(X,Y,"r")
p.plot(X,Y,"r.")
p.title("log(Error) vs. log(nts) using Runge-Kutta")
p.xlabel("log(nts)",fontsize=16)
p.ylabel("log(Error)", fontsize=16)
p.show()
p.savefig("rkerrorplot.png")