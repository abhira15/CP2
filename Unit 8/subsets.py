def bt(set1,subset,index):
    print("{",*subset,"}")   
    for i in range(index,len(set1)):
        subset.append(set1[i])
        bt(set1,subset,i+1)
        subset.pop(-1)
set1 = list(map(int,input().split(" ")))
subset = []
index = 0
bt(set1,subset,index) 