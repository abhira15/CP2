from collections import defaultdict

class Node_Distance :

    def __init__(self, name, dist) :
        self.name = name
        self.dist = dist

class Graph :

    def __init__(self, node_count) :
        # Store the adjacency list as a dictionary
        # The default dictionary would create an empty list as a default (value) 
        # for the nonexistent keys.
        self.adjlist = defaultdict(list)
        self.node_count = node_count

    def Add_Into_Adjlist(self, src, node_dist) :
        self.adjlist[src].append(node_dist)

    def Dijkstras_Shortest_Path(self, source) :

        # Initialize the distance of all the nodes from the source node to infinity
        distance = [999999999999] * self.node_count
        # Distance of source node to itself is 0
        distance[source] = 0

        # Create a dictionary of { node, distance_from_source }
        dict_node_length = {source: 0}

        while dict_node_length :

            # Get the key for the smallest value in the dictionary
            # i.e Get the node with the shortest distance from the source
            current_source_node = min(dict_node_length, key = lambda k: dict_node_length[k])
            del dict_node_length[current_source_node]

            for node_dist in self.adjlist[current_source_node] :
                adjnode = node_dist.name
                length_to_adjnode = node_dist.dist

                # Edge relaxation
                if distance[adjnode] > distance[current_source_node] + length_to_adjnode :
                    distance[adjnode] = distance[current_source_node] + length_to_adjnode
                    dict_node_length[adjnode] = distance[adjnode]

        for i in range(self.node_count) :
            answer.append([source,i,distance[i]])

def main() :
    p2=[]
    station = []
    stations, intersections = map(int,input().split())
    for i in range(stations):
        station.append(int(input()))
    List = []
    global answer
    answer = []    
    for i in range(intersections):
        x = list(map(int,input().split()))
        List.append(x)
        
    #print(List)
        
    for smallerList in List:
        for index, number in enumerate(smallerList):
            if index ==2:
                continue
            smallerList[index] = smallerList[index]-1
            
    #print(List)

    g = Graph(intersections)
    for point in List:    
        g.Add_Into_Adjlist(point[0], Node_Distance(point[1], point[2]))
        g.Add_Into_Adjlist(point[1], Node_Distance(point[0], point[2]))
        
    for fire in station:
        g.Dijkstras_Shortest_Path(fire-1)
        
    p2=[]
    FireStation=[]
    #print(answer)
    for maximum in answer:
        p2.append(maximum[2])
    maxi = max(p2)
    #print(p2)
    for ans in answer:
        if ans[2] == maxi:
            FireStation.append(ans[1]+1)
    fireStation = sum(FireStation)/len(FireStation)
    print(int(fireStation))       
    print("")
    
if __name__ == "__main__" :
   main()

