##Colt Bradley
#3.15.2016
#Lesson 20.2

import os
os.chdir("C:/Users/Colt/OneDrive/Documents/Professional/School/16spring/PY_251/20.FourierAnalysis")

#############################################################################
#functions and modules
#############################################################################
#import modules
import numpy as n
import pylab as p

#define essential functions
 #These compute the real/complex parts of the fourier transform        
def fourReal(f,x,t):
    y = f(x)*n.cos(2*n.pi*x*t)
    return y
def fourComp(f,x,t):
    y = -f(x)*n.sin(2*n.pi*x*t)
    return y
    
def a(x):
    y = n.sin(6*n.pi*3*x)*n.exp(-x**2)
    return y

#############################################################################
#Homework 2
#############################################################################
t = n.linspace(-4,4,100)
dt = t[1]-t[0]
func3 = []

for k in t:
    func3.append(a(k))

#computes the discrete transform
A = n.fft.fft(func3)
#changes time values to frequency
freq = n.fft.fftfreq(len(t),dt)

p.close()
p.plot(t,func3,"b")
p.title("Part 2 Function Graph")
p.xlabel("Time (s)",fontsize = 16)
p.ylabel("Function Value",fontsize = 16)
p.savefig("prt2_function.png")
p.show()

p.close()
p.plot(freq,n.real(A),"b")
p.title("Part 2 Fourier Transform - Real Part")
p.xlabel("Frequency (Hz)",fontsize = 16)
p.ylabel("Function Value",fontsize = 16)
p.savefig("prt2_fourReal.png")
p.show()

p.close()
p.plot(freq,n.imag(A),"b")
p.title("Part 2 Fourier Transform - Imaginary Part")
p.xlabel("Frequency (Hz)",fontsize = 16)
p.ylabel("Function Value",fontsize = 16)
p.savefig("prt2_fourComp.png")
p.show()