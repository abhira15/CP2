from collections import defaultdict
test_case = int(input())
count = 1
while(test_case>0):
    n = int(input())
    vertex = []
    for i in range(n):
        x = list(map(int,input().split()))
        vertex.append(x)
    Total_vertex = max(max(vertex))
    #print(vertex)
    for smallerList in vertex:
        for index, number in enumerate(smallerList):
            smallerList[index] = smallerList[index]-1
    #print(vertex)        
#code from geeks for Eulerian Path 
    class Graph:

        def __init__(self,vertices):
            self.V= vertices #No. of vertices
            self.graph = defaultdict(list) # default dictionary to store graph
            self.Time = 0

        def addEdge(self,u,v):
            self.graph[u].append(v)
            self.graph[v].append(u)

        def rmvEdge(self, u, v):
            for index, key in enumerate(self.graph[u]):
                if key == v:
                    self.graph[u].pop(index)
            for index, key in enumerate(self.graph[v]):
                if key == u:
                    self.graph[v].pop(index)


        def DFSCount(self, v, visited):
            count = 1
            visited[v] = True
            for i in self.graph[v]:
                if visited[i] == False:
                    count = count + self.DFSCount(i, visited)       
            return count

        def isValidNextEdge(self, u, v):


            if len(self.graph[u]) == 1:
                return True
            else:
  
                visited =[False]*(self.V)
                count1 = self.DFSCount(u, visited)


                self.rmvEdge(u, v)
                visited =[False]*(self.V)
                count2 = self.DFSCount(u, visited)

                self.addEdge(u,v)

                return False if count1 > count2 else True

        def printEulerUtil(self, u):

            for v in self.graph[u]:

                if self.isValidNextEdge(u, v):

                    List.append([u,v])  
                    self.rmvEdge(u, v)
                    self.printEulerUtil(v)

        def printEulerTour(self):

            u = 0
            for i in range(self.V):
                if len(self.graph[i]) %2 != 0 :
                    u = i
                    break

            
            self.printEulerUtil(u)

    g1 = Graph(Total_vertex)
    for point in vertex:    
        g1.addEdge(point[0],point[1])

    global List
    List = []
    g1.printEulerTour()
    #print(List)
    for smallerList in List:
        for index, number in enumerate(smallerList):
            smallerList[index] = smallerList[index]+1
    #print(List)      
    print(f"Case #{count}")
    if(List[0][0] == List[-1][1]):
        for point in List:
            print(point[0],point[1])
        print("")
    else:
        print("some beads may be lost\n")

    test_case-=1
    count+=1
    #This code is contributed by Neelam Yadav
