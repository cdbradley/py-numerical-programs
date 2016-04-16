##Colt Bradley
#3.15.2016
#Lesson 15

import os
os.chdir("C:/Users/Colt/OneDrive/Documents/Professional/School/16spring/PY_251/Lesson 20")

#############################################################################
#functions and modules
#############################################################################
#import modules
import numpy as n
import pylab as p

#define essential functions
#first is used in the first homeowrk exercise
def f(x):
    y = n.sin(6*n.pi*x)*n.exp(-x**2)
    return y
    
def ff(x,t):
    y = n.sin(6*n.pi*x)*n.exp(-x**2)*n.exp(-2*n.pi*1j*x*t)
    return y
    
def g(x):
    y = n.cos(6*n.pi*x)*n.exp(-x**2)
    return y
    
def a(x):
    y = n.sin(6*n.pi*3*x)*n.exp(-x**2)
    return y

def gf(x,t):
    y = n.cos(6*n.pi*x)*n.exp(-x**2)*n.exp(-2*n.pi*1j*x*t)
    return y

#fucntion simpson() is the simpson rule function
def simpsonfor(f,t,a,b,N):
    h = float(b-a)/N
    i = 1
    n = 1
    
    I_1 = 0.
    while i < N:
        I_1 += f(a+i*h,t)
        i += 1
    
    I_2 = 0   
    while n < N+1:
        I_2 += f(a+n*h - h/2,t)
        n += 1
    return (h/6)*(f(a,t)+f(b,t)+2*I_1+4*I_2)


#############################################################################
#Homework 1
#############################################################################

#create a list of times
t1 = n.linspace(-4,4,num = 800)
func1 = []
func2 = []

for i in t1:
    func1.append(f(i))
    
for i in t1:
    func2.append(g(i))
    

#create a list to contain I, create a list for select numbers between the error
#function bounds
I1 = []
I2 = []
ns = n.linspace(-6,6, num = 800)
t2 = n.linspace(-6,6,num = 800)

#compute the error function for various numbers
for i in ns:
    k = simpsonfor(ff,i,-4,4,800)
    I1.append(k)
    
for i in ns:
    k = simpsonfor(gf,i,-4,4,800)
    I2.append(k)

p.close()
p.plot(t1,func1,"b")
p.title("Function 1 graph")
p.xlabel("time (s)",fontsize = 16)
p.ylabel("Function Value",fontsize = 16)
p.savefig("hw1fgraph.png")
p.show()

p.close()
p.plot(t1,func2,"b")
p.title("Function 2 graph")
p.xlabel("time (s)",fontsize = 16)
p.ylabel("Function Value",fontsize = 16)
p.savefig("hw1ggraph.png")
p.show()

p.close()
p.plot(t2,I1,"b")
p.title("Function 1 fourier transform")
p.xlabel("time (s)",fontsize = 16)
p.ylabel("Function Value",fontsize = 16)
p.savefig("hw1transformfgraph.png")
p.show()

p.close()
p.plot(t2,I2,"b")
p.title("Function 2 fourier transform")
p.xlabel("time (s)",fontsize = 16)
p.ylabel("Function Value",fontsize = 16)
p.savefig("hw1transformggraph.png")
p.show()

#############################################################################
#Homework 2
#############################################################################
t3 = n.linspace(-4,4,100)
func3 = []

for k in t3:
    func3.append(a(k))

A = n.fft.fft(func3)

p.close()
p.plot(t3,func3,"b")
p.title("Function 1 graph")
p.xlabel("time (s)",fontsize = 16)
p.ylabel("Function Value",fontsize = 16)
p.savefig("hw2agraph.png")
p.show()

p.close()
p.plot(t3,A,"b")
p.title("Function 1 fourier transform")
p.xlabel("time (s)",fontsize = 16)
p.ylabel("Function Value",fontsize = 16)
p.savefig("hw2transformagraph.png")
p.show()

#############################################################################
#Homework 3
#############################################################################