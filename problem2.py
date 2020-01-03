def fiboEvenSum(number):
    arr=[1,2]
    sum=arr[1]
    for i in range(2,number):
        n=arr[i-1]+arr[i-2]
        arr.append(n)
        if(n%2==0):
            sum+=n
    return(sum)
    pass

print(fiboEvenSum(int(input())))
