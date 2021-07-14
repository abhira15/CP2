def twar(a , t1 , t2 , i):
    global maximum
    
    if (i == len(a)):
        diff = abs(sum(t1) - sum(t2))
        if ( maximum > diff ):
            maximum  = diff
            #print(t1,t2)
            if sum(t2)>sum(t1):print(sum(t1) , "" , sum(t2))
            else : print(sum(t2) , "" , sum(t1))
            
    else:
     if (len(t1) < (len(a)+1)/2):
        t1.append(a[i])
        twar(a , t1 , t2 , i+1)
        t1.pop(-1)

     if (len(t2) < (len(a)+1)/2):
        t2.append(a[i])
        twar(a , t1 , t2 , i+1 )
        t2.pop(-1)

while True:
    array = list(map(int,input().split(" ")))
    team1 = []
    team2 = []
    maximum = max(array)
    twar(array , team1 , team2 , 0 )



