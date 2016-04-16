#Colt Bradley
#Test 1, Problem 2

#Ask user for N_Max
n_max = raw_input("Please give an integer: ")
n_max = int(n_max)

for r in  range(1,n_max+1):
    an = 0
    for n in range(1,r+1):
        num = ((-1)**(n+1))
        num = float(num)
        den = (2*n-1)
        an = an+ 4*num/den
    print "{}: {}" .format(r,an)
