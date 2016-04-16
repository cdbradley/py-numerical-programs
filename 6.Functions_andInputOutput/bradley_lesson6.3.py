#Colt Bradley
#1.31.16
#playing around with the last bit of lesson 6

#import essential packages
import numpy as n

#open file
filehandle = open("lesson6_data.txt","r")

#manipulate
#string = filehandle.read()
#line = filehandle.readline()
lines = filehandle.readlines()
for i in range(0,10):
    print lines[i]
    
filehandle.close()