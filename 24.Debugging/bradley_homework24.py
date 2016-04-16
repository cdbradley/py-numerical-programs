#Colt Bradley
#3.22.2016
#Lesson 24


#############################################################################
#functions and modules
#############################################################################

#import modules
import numpy as n
import pylab as p

def pentagonal(n):
    return n*(3*n-1)/2.
    
#Checks to see if the sum of two elements of list a and b is in list c, then
#prints that list
def compare(a,b,c):
    pents = []
    K = []
    N = []
    for i in a:
        for k in b:
            for n in c:
                summ = k+n
                
                if summ == i:
                    pents.append(summ)
                    K.append(k)
                    N.append(n)
                    break
    pairs = zip(K,N)
    return pairs  

#############################################################################
#Exercise 1
#############################################################################

#first, create a list of all pentagonal numbers
n1 = n.linspace(1,50)
pent = []
for i in n1:
    pent.append(pentagonal(i))
    
#creates a longer list of pentagonal numbers for comparison beyond n=50
n2 = n.linspace(1,100,100)
pent2 = []
for i in n2:
    pent2.append(pentagonal(i))
    
#now, compare using compare function
A = compare(pent2,pent,pent)

#Delete the commutative duplicates using sets
seen = set()
new_pents = []
for item in A:
    item_set = frozenset(item)
    if item_set not in seen:
        new_pents.append(item)
        seen.add(item_set)
print new_pents