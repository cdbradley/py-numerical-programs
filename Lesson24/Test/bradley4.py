#Colt Bradley
#Test1, Problem 4

import numpy as n

x0 = 1.
v0 = 0.
t0 = 0.
tf = 10.
nts = 50000000
dt = (tf-t0)/nts

t = n.linspace(t0,tf,num=nts+1)
X = n.zeros(len(t))
V = n.zeros(len(t))

X[0]= x0
V[0]= v0
for i in range(0,nts):
    X[i+1] = X[i] + V[i]*dt
    V[i+1] = V[i] - X[i]*dt

print X[-1]

#To determine what is reliable, I run the code at different time steps and see how the answer changes. For example, some data is below, in the format "nts: X[-1]"
#1000: -.88228
#2000: -.86036
#4000: -.84963
#8000: -.84433
#16000: -.84169
#32000: -.84038
#64000: -.83972
#128000: -.83939
#1280000: -.83910
#Since we know that each time nts doubles, the error doubles, we obviously want to trust the larger time steps. To what degree is the question. Judging by this, I would certainly
#trust the -.83 value. The .009 part is questionable, but I think it's close. We coudl decide after another analysis of time steps. 