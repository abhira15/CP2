def isSafe(x,y):
    global lst1
    for i in range(x,-1,-1):
        if lst1[i][y]==1:
            return False
    row=x
    col=y
    while row>=0 and col>=0:
        if lst1[row][col]==1:
            return False
        row-=1
        col-=1

    row=x
    col=y
    while row>=0 and col<len(lst1):
        if lst1[row][col]==1:
            return False
        row-=1
        col+=1

    return True


def nQueen(x):
    global count
    global lst1
    if x == len(lst1):
        count+=1
        print("solution"+str(count)+":")
        for i in lst1:
            print(i)
        print()
    if x>=len(lst1):
        return True
    for col in range(len(lst1)):
        if isSafe(x,col):
            lst1[x][col]=1
            nQueen(x+1)
            lst1[x][col]=0
     
    return False


n=int(input())
lst1=[]
for i in range(n):
    lst1.append([0]*n)

count=0    
if nQueen(0):
    for i in lst1:
        print(i)
print(count)