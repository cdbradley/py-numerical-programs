##Colt Bradley
#3.15.2016
#Lesson 20.1

import os
os.chdir("C:/Users/Colt/OneDrive/Documents/Professional/School/16spring/PY_251/20.FourierAnalysis")

#############################################################################
#functions and modules
#############################################################################
#import modules
import numpy as n
import pylab as p

#define essential functions
#first two are used in the first homeowrk exercise
def f(x):
    y = n.sin(6*n.pi*x)*n.exp(-x**2)
    return y
def g(x):
    y = n.cos(6*n.pi*x)*n.exp(-x**2)
    return y

    #These compute the real/complex parts of the fourier transform        
def fourReal(f,x,t):
    y = f(x)*n.cos(2*n.pi*x*t)
    return y
def fourComp(f,x,t):
    y = -f(x)*n.sin(2*n.pi*x*t)
    return y

#fucntion simpsonfour() is the simpson rule function specifically for fourier
def simpsonfour(f,g,t,a,b,N):
    h = float(b-a)/N
    i = 1
    n = 1
    
    I_1 = 0.
    while i < N:
        I_1 += f(g,a+i*h,t)
        i += 1
    
    I_2 = 0   
    while n < N+1:
        I_2 += f(g,a+n*h - h/2,t)
        n += 1
    return (h/6)*(f(g,a,t)+f(g,b,t)+2*I_1+4*I_2)


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
fReal = []
fComp = []
gReal = []
gComp = []
freq = n.linspace(-6,6,num = 800)

#compute the fourier transform for Real/complex part
for i in freq:
    k = simpsonfour(fourReal,f,i,-4,4,800)
    fReal.append(k)   
for i in freq:
    k = simpsonfour(fourComp,f,i,-4,4,800)
    fComp.append(k)
    
for i in freq:
    k = simpsonfour(fourReal,g,i,-4,4,800)
    gReal.append(k)
for i in freq:
    k = simpsonfour(fourComp,g,i,-4,4,800)
    gComp.append(k)
    
#Graph a(t) vs t for both functions
p.close()
p.plot(t1,func1,"b")
p.title("Graph of Sin-Exponential function")
p.xlabel("time (s)",fontsize = 16)
p.ylabel("Function Value",fontsize = 16)
p.savefig("sin_wavepacket.png")
p.show()

p.close()
p.plot(t1,func2,"b")
p.title("Graph of Cos-Exponential function")
p.xlabel("time (s)",fontsize = 16)
p.ylabel("Function Value",fontsize = 16)
p.savefig("cos_wavepacket.png")
p.show()

#Graph A(f) vs f real part
p.close()
p.plot(freq,fReal,"b")
p.title("Sin-Exponential Fourier Transform Real part")
p.xlabel("Frequency (Hz)",fontsize = 16)
p.ylabel("Function Value",fontsize = 16)
p.savefig("sin_fourReal.png")
p.show()

p.close()
p.plot(freq,gReal,"b")
p.title("Cos-Exponential Fourier Transform Real part")
p.xlabel("Frequency (Hz)",fontsize = 16)
p.ylabel("Function Value",fontsize = 16)
p.savefig("cos_fourReal.png")
p.show()

#Graph A(f) vs f Complex part
p.close()
p.plot(freq,fComp,"b")
p.title("Sin-Exponential Fourier Transform Complex part")
p.xlabel("Frequency (Hz)",fontsize = 16)
p.ylabel("Function Value",fontsize = 16)
p.savefig("sin_fourComp.png")
p.show()

p.close()
p.plot(freq,gComp,"b")
p.title("Cos-Exponential Fourier Transform Complex part")
p.xlabel("Frequency (Hz)",fontsize = 16)
p.ylabel("Function Value",fontsize = 16)
p.savefig("cos_fourComp.png")
p.show()
