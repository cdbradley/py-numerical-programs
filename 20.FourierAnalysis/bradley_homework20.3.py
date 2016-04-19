##Colt Bradley
#3.15.2016
#Lesson 20.3

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

#############################################################################
#Homework 3
#############################################################################
time,amp = n.loadtxt("Lesson20_Data.txt",usecols = (0,1), unpack =True)
dt = time[1]-time[0]
power = []
N = len(time)

#computes the discrete transform
A = n.fft.fft(amp)
#changes time values to frequency
freq = n.fft.fftfreq(N,dt)

power.append((1.0/N**2)*((A[0]*n.conj(A[0]))))
for i in range(1,N/2-1):
    power.append((1.0/N**2)*((A[i]*n.conj(A[i]))+(A[N-i]*n.conj(A[N-i]))))

power.append((1.0/N**2)*((A[N/2]*n.conj(A[N/2]))))

#create plots
p.close()
p.plot(time,amp,"b")
p.title("Part 3 Function Graph")
p.xlabel("Time (s)",fontsize = 16)
p.ylabel("Function Value",fontsize = 16)
p.savefig("prt3_function.png")
p.show()

p.close()
p.plot(freq[:N/2+dt],power,"b")
p.title("Periodogram")
p.xlabel("Frequency (Hz)",fontsize = 16)
p.ylabel("Power",fontsize = 16)
p.savefig("prt3_periodogram.png")
p.show()

