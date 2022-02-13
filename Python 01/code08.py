def isprime(num):
    for n in range(2,int(num**1/2)+1):
        if num%n==0:
            print("not prime")
            return()
    print("prime")
    return()
    
isprime(int(input()))
