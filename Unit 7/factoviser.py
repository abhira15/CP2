import math 
while True:
    n,m = map(int,input().split())
    if n == 0 or m == 0:
        break
    else:
        fact = math.factorial(n)
        print(f"{m} divides {n}!"
              if fact % m == 0
              else f"{m} does not divide {n}!")
    