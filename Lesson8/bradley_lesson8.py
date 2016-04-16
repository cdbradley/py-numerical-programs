#Colt Bradley
#2.4.16
#Working through lesson 8

#import packages
import numpy as n

tau = 5.            #Mean lifetime
Ninitial = 100.     #initial number of nuclei
tinitial = 0.       #initial time
tfinal = 2.         #final time
nts = 10           #number of timestamps
dt = (tfinal - tinitial)/nts

#create an array to hold times and numbers
t = n.linspace(tinitial, tfinal,num = nts+1)
N = n.zeros(len(t))

#Evolve with Euler's method
N[0] = Ninitial
for i in range(0,nts):
    N[i+1] = N[i] - N[i]*dt/tau
    print "at time t = {:.3f}, N = {:.3f}" .format(t[i+1],N[i+1])
    
error =(67.032-N[-1])/67.032
print
print error