#bicoloring

from collections import deque

def load_graph():
    """Load graph into its adjacency list"""
    vertices = int(input())
   
    # Check it is a valid graph and not the end of the file
    if vertices==0:
        return None

    # Load each edge an construct adjcency  list
    edges = int(input())
   
    adjList = [list() for v in range(vertices)]

    for i in range(edges):
        s, e = list(map(int,input().split()))
        adjList[s].append(e)
        adjList[e].append(s)
    return adjList


def is_bicolored(adjList):
    
    vertices = len(adjList)
    
    discovered = [False for x in range(vertices)]
    processed = [False for x in range(vertices)]
    color = [False for x in range(vertices)]

    q = deque([0])
    color[0] = 0

    while q:
        v = q.popleft()
        processed[v] = True

        for n in adjList[v]:

            if not discovered[n]:
                discovered[n] = True
                color[n] = 0 if color[v] else 1
                q.append(n)
            elif color[n]==color[v]:
                return False
        

    return True

while True:
    adj = load_graph()
    if not adj:
        break

    if is_bicolored(adj):
        print("BICOLORABLE.")
    else:
        print("NOT BICOLORABLE.")

