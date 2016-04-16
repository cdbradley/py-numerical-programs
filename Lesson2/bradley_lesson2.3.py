#Colt Bradley
#1.14.16
#Height of an object thrown vertically up

# time that we want the position in seconds
t = raw_input('Time in seconds:') 
t = float(t)

#initial velocity in meters/sec
v0= raw_input('Initial velocity in m/s')
v0 = float(v0)

g=9.8 #little g

y=v0*t - .5*g*t**2 #vertical position

print "The height at t = {} seconds is y = {} meters" .format(t,y)
