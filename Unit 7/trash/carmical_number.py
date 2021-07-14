
# A Python program to check if a number is 
# Carmichael or not. 
  
# utility function to find gcd of two numbers 
def gcd( a, b) : 
    if (a < b) : 
        return gcd(b, a) 
    if (a % b == 0) : 
        return b 
    return gcd(b, a % b) 
  
# utility function to find pow(x, y) under 
# given modulo mod 
def power(x, y, mod) : 
    if (y == 0) : 
        return 1
    temp = power(x, y / 2, mod) % mod 
    temp = (temp * temp) % mod 
    if (y % 2 == 1) : 
        temp = (temp * x) % mod 
    return temp 
  
  
# This function receives an integer n and 
# finds if it's a Carmichael number 
def isCarmichaelNumber( n) : 
    b = 2
    while b<n : 
          
        # If "b" is relatively prime to n 
        if (gcd(b, n) == 1) : 
  
            # And pow(b, n-1)% n is not 1, 
            # return false. 
            if (power(b, n - 1, n) != 1): 
                return "The number " + str(n) + " is a Carmichael number."
        b = b + 1
    return str(n) + " is normal."
  
 
  
while True:
    n = int(input())
    if n == 0 :
        break
    else:
       print(isCarmichaelNumber(n))
    
    




