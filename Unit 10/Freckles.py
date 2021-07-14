import math
from collections import defaultdict
def distance(x1 , y1 , x2 , y2):

    result = math.sqrt(math.pow(x2 - x1, 2) +
                math.pow(y2 - y1, 2) * 1.0)
    return round(result,2)

n = int(input())
List = []
for i in range(n):
    x = list(map(float,input().split()))
    List.append(x)

two_vertex= []
for i in List:
    for k in List:
        j = [i,k]
        j.sort()
        if (i==k) or j in two_vertex:
            continue
        two_vertex.append(j)
#print(two_vertex)
total_edge = n * (n - 1)/2
for i in range(int(total_edge)):
    points = two_vertex[i]
    two_vertex[i].append(distance(points[0][0],points[0][1],points[1][0],points[1][1]))
    
#print(two_vertex)

#ashwins code 
counterList = []
for smallerList in two_vertex:
    for index, eachList in enumerate(smallerList):
        if type(eachList) == type([]):
            if eachList in counterList:
                smallerList[index] = counterList.index(eachList)
            else:
                smallerList[index] = len(counterList)
                counterList.append(eachList)
#print(two_vertex)               
# Class to represent a graph

class Graph:

    def __init__(self, vertices):
        self.V = vertices # No. of vertices
        self.graph = [] # default dictionary
        # to store graph

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # The main function to construct MST using Kruskal's
        # algorithm
    def KruskalMST(self):

        result = [] # This will store the resultant MST
        
        # An index variable, used for sorted edges
        i = 0
        
        # An index variable, used for result[]
        e = 0

        # Step 1: Sort all the edges in
        # non-decreasing order of their
        # weight. If we are not allowed to change the
        # given graph, we can create a copy of graph
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:

            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge does't
            # cause cycle, include it in result
            # and increment the indexof result
            # for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge

        minimumCost = 0
        for u, v, weight in result:
            minimumCost += weight
        print("The minimum total length of ink lines that can connect all the freckles is" , round(minimumCost,2))

# Driver code
g = Graph(n)
for point in two_vertex:    
    g.addEdge(point[0],point[1], point[2])
# Function call
g.KruskalMST()
# This code is contributed by Neelam Yadav



    
    
    

            
    
