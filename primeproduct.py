# Write a Python function primeproduct(m) that takes an integer m as input and returns True if m is a prime product and False otherwise. (If m is not positive, your function should return False.) 

def primeproduct(m):
    factor=[]
    for i in range (1,m+1):
        if(m%i==0):
           factor.append(i)
    if(len(factor)<=4):
        return True
    else:
        return False
