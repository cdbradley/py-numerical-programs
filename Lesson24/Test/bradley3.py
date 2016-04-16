#Colt Bradley
#Test 1, Problem 3

import numpy as n
import pylab as p

a = n.loadtxt("ligodata")
time = a[:,0]
amp = a[:,1]

#Units are assumed, units for amplitude are unknown
p.close()
p.plot(time,amp,"r.")
p.title("Data from Ligo Detector")
p.xlabel("Time (seconds)", fontsize=16)
p.ylabel("Amplitude", fontsize=16)
p.show()