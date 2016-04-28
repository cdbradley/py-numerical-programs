#Colt Bradley
#4.28.16
#PY251 Final
#question4

#import modules
import numpy as np
import pylab as py
from scipy.optimize import curve_fit


def func(x,a,b,c,d):
    return a*x**3+b*x**2+c*x+d

Xd, Yd = np.loadtxt("somedata", usecols = (0, 1), unpack = True)
par, con = curve_fit(func,Xd,Yd)

sin=[]
for i in Xd:
    y = func(i,par[0],par[1],par[2],par[3])
    sin.append(y)

py.close()
py.plot(Xd,Yd,"r.")
py.plot(Xd,sin,"r")
py.title("Least squares fit for Somedata")
py.xlabel("y")
py.ylabel("x")
py.savefig("somedata.png")
py.show()