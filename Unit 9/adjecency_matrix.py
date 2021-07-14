# Adjacency Matrix representation in Python
class Graph(object):
    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
    # Add edges
    def add_edge(self, v1, v2):
        
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    # Print the matrix
    def print_matrix(self):
        count=0
        for row in self.adjMatrix:
            print(count,end=" ")
            for val in row:
                print('{:4}'.format(val),end=" "),
            print()
            count+=1
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(3, 0)
print("{:1}".format(" "),end=" ")
for i in range(0,4):
    print('{:4}'.format(i),end=" "),
print()
g.print_matrix()
