# number of terms in the series
nterm= 15
f=0
#First two terms of series
n1,n2=0,1
# GENERATE Fibonacci series
while f<nterm:
    print(n1)
    n3=n1+n2
    #updating values
    n1=n2
    n2=n3
    f+=1