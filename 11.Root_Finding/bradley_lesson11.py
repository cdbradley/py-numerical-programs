#Colt Bradley
#2.23.16
#Working through lesson 11

import numpy as n
import pylab as p

k = .02
g = 9.8
v = 35.

def f(t):
    ans = -(g*t/k) + (v+g/k)/k*(1-n.e**(-k*t))
    return ans
    
def fprime(t):
    ans = -(g/k) + (v+g/k)/k*(k*n.e**(-k*t))
    return ans 

#guessing
a = 1
t = 6
while a > 0:
    a = f(t)
    t = t +.001
    
print a
print t

#Newton

guess = 5
guesses = [0]
guesses.append(guess)

x = guesses[1] - f(guesses[1])/fprime(guesses[1])
tolerance = .0000000001

while abs(guesses[-1]-guesses[-2])>= tolerance:
    x = guesses[-1] - f(guesses[-1])/fprime(guesses[-1])
    guesses.append(x)
    
print 
print x