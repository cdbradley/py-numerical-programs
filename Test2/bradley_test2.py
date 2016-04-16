#Colt Bradley
#3.29.16
#Test 2

#import modules and functions
import numpy as n
import pylab as p
    
#function to calculate central difference
def central_difference(f,x,h):
    deriv = (f(float(x+h))-f(float(x-h)))/(2.*h)
    return deriv
    
#fucntion simpson() is the simpson rule function
def simpson(f,a,b,N):
    h = float(b-a)/N
    i = 1
    n = 1
    
    I_1 = 0.
    while i < N:
        I_1 += f(a+i*h)
        i += 1
    
    I_2 = 0   
    while n < N+1:
        I_2 += f(a+n*h - h/2)
        n += 1
    return (h/6)*(f(a)+f(b)+2*I_1+4*I_2)
    
#Newton's Method
def newton(f,fp):
    guess = 5
    guesses = [0]
    guesses.append(guess)

    #iterate once to check the value adds correctly, define tolerance
    x = guesses[1] - (f(guesses[1]))/fp(guesses[1])
    tolerance = .0000000001

    #create a while loop that runs while answers are outside a specified tolerance
    while abs(guesses[-1]-guesses[-2])>= tolerance:
        x = guesses[-1] - (f(guesses[-1]))/fp(guesses[-1])
        guesses.append(x)
    return guesses[-1]


###############################################################################
#Problem 1
###############################################################################    
x0 = 0
y0 = 0
x = x0
y = y0
tf = 4.
ts = 1000
dt = tf/ts
Y = []
X = []
time = []
t = 0

for i in range(0, ts):
    #do first step
    x1 = x + (y+t-1)*dt/2
    y1 = x + (x-t+1)*dt/2
    
    #do second step
    x = x + (y1+t-1)*dt
    y = y + (x1-t+1)*dt
    
    #interate values and append solutions to a list
    t = t +dt
    X.append(x)
    Y.append(y)
    time.append(t)
    
#create and save plot for the height
p.close()
p.plot(time,Y,"r")
p.title("Plot of Y values")
p.ylabel("Y Value", fontsize = 16)
p.xlabel("Time (s)",fontsize = 16)
p.show()
p.savefig("Y.png")

#create and save plot for velocity
p.close()
p.plot(time,X,0,"r")
p.title("Plot of X values")
p.ylabel("X value", fontsize = 16)
p.xlabel("Time (s)",fontsize = 16)
p.show()
p.savefig("X.png")

#X(4) = -4.
#The error goes as dt^2, so the error is proportional to 1.6e-5   
                        
###############################################################################
#Problem 2
###############################################################################
def g(x):
    return n.exp(-(x**2))-x
    
def gp(x):
    return -2*x*n.exp(-(x**2))-1

print newton(g,gp)

#Answer is: 0.65292

###############################################################################
#Problem 3
###############################################################################
def f(x):
    return n.sin(n.exp(x))
    
print simpson(f,-3,3.,100.)

#Answer is: 1.50241
#Error for simposon's rule goes as 1/N^4, so the error is proportional to 1/100000000
#This means that the result is very resonabily accurate

###############################################################################
#Problem 4
###############################################################################
Xd, Yd = n.loadtxt("problem4data", usecols = (0, 1), unpack = True)

p.close()
p.plot(Xd,Yd,"r")
p.show()
print
print (Yd[103]-Yd[97])/(Xd[103]-Xd[97])
print (Yd[203]-Yd[197])/(Xd[203]-Xd[197])

#I don't remember how to do this in a better, way, but these are very loose approximations of what the values should be. 