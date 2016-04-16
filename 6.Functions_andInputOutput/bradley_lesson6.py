#Colt Bradley
#1.28.16
#Lesson 6 working through

import bradley_functions as f

N = raw_input("Give me an integer as a base: ")
N = int(N)

r = raw_input("Give me an integer as an exponent: ")
r = int(r)

print f.power(f.factorial(N),r)