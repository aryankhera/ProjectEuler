import math
def largestPrimeFactor(number):
    i=2
    while(i<=number):
        if number%i==0:
            number=number/i
            i-=1
        i+=1
    return(int(i))
    pass

def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
    pass
print(largestPrimeFactor(int(input())))
