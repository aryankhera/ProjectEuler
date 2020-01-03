def multiplesOf3and5(number):
    sum=0
    for i in range(1,number):
        sum+=i if i%15==0 else (i if i%3==0 else (i if i%5==0 else 0)) 
    return(sum)
    pass

print(multiplesOf3and5(int(input())))
