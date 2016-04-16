#Colt Bradley
#3.3.16
#Lesson 14

import numpy as n
import pylab as p

a = 0
b = n.pi/2
N = 20
h = (b-a)/N
I_m = 0
i = 1
I = []
err = []

r = n.zeros(N)
r[0] = 2
for i in range(0,N-1):
    r[i+1] = 2*r[i]

#middle
for k in r:
    i = 0
    I_m = 0
    while i < k+1:
        I_m = I_m + n.sin(a+i*h-h/2)*h
        i = i+1
    I.append(I_m)
    err.append(abs(1-I_m))

err = n.log(err)
#r = n.log(r)

p.plot(r,err,"r")
p.show()

