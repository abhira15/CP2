def load_graph():
    """Load graph into its adjacency list"""
    global vertices

    if vertices==0:
        return None

    edges = int(input())
   
    adjList = [list() for v in range(vertices)]

    for i in range(edges):
        s, e = list(map(int,input().split()))
        adjList[s].append(e)
        adjList[e].append(s)
    return adjList
    

vertices = int(input())
adj = load_graph()

for i in range(vertices):
    print("Vertex " + str(i) + ":", end="")
    for j in adj[i]:
        print(" -> {}".format(j), end="")
    print("\n")








