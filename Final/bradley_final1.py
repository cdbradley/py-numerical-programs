#Colt Bradley
#4.28.16
#PY251 Final
#question1

#import modules
import numpy as np
import pylab as py

def F(n):
    N = 0
    for k in range(1,n+1):
        N=N+k**(-n/2)
    return N
    
t = range(1,10)
X=[]

for i in t:
    X.append(F(i))
    
py.close()
py.plot(t,X)
py.show()

print F(2)
#n=2 gives highest value
#F(2) = 1.5