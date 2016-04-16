#Colt Bradley
#1.14.16
#Height of an object thrown vertically up

t=2. # time that we want the position in seconds
v0=10. #initial velocity in meters/sec
g=9.8 #little g

y=v0*t - .5*g*t**2

print y
print "The height at t = {} seconds is y = {} meters" .format(t,y)
print "The height at t = ", t, "seconds is y = ", y, "meters"
print "the height at t = "+str(t)+" seconds is y = "+str(y)+" meters"