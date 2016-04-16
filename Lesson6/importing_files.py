import numpy as n

data1 = n.loadtxt("data1.txt")
data2 = n.loadtxt("data2.txt")
c = n.loadtxt("array.txt")


print data1
print
print data2
print
print c
print c[0,1]
print c[1,0]
print c[:,0]
n.savetxt("testsave.txt",zip(c[:,0],c[:,2]))
print n.loadtxt("testsave.txt")