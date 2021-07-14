import math;

#create a list of prime number upto given number
def prime_upto(n):  
    lower = 2 
    upper = n
    l = []
    for num in range(lower,upper + 1):  
       if num > 1:  
           for i in range(2,num):  
               if (num % i) == 0:  
                   break  
           else:
               l.append(num)
    return l

#check if the number is prime or not
def isPrime(x): 
    s = int(math.sqrt(x)) 
    for i in range(2,s+1): 
        if (x % i == 0): 
            return False
    return True

#main
while True:
    n = int(input())
    #check for the exceptions and end the program
    if n == 0:
        break
    if(n <= 7): 
        print("Impossible to form")
        continue
    # if number is even
    if n%2 == 0:
        a = 2
        b = 2
        num = n - 4
    #if number is odd
    else :
        a = 2
        b = 3
        num = n - 5

    prime = prime_upto(num)
    prime.reverse()

    for i in prime:
        c = num - i
        if isPrime(c) and c != 1 :
            d = i
            print(b,d,c,a)
            break    

