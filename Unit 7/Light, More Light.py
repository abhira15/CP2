from math import sqrt

while True:
  num = int(input())
  if num == 0:
    break
  sav = sqrt(num)
  
  print("yes" if sav == int(sav) else "no")
  
  