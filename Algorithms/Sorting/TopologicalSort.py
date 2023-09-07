# Algorithm
# Topological Sort 

'''
If a vetrex depends on current vertex then go to that vertex and push it in stack. Then come back to current vertex.
Start with a vertex -- loop for all vertex
Find if vertex is visited and if not then find edges of it using utility function

'''
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        #self.numberofVertices = numberofVertices


    def __str__(self):
        values = [k for k in self.graph]
        return ",".join(values)


    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)


    def topologicalSortUtl(self, v, visited, stack):
        visited.append(v)
        for e in self.graph[v]:
            if e not in visited:
                self.topologicalSortUtl(e,visited,stack)
                
        stack.insert(0,v)


    def topologicSort(self):

        visited = []
        stack = []

        for v in list(self.graph):
            if v not in visited:
                self.topologicalSortUtl(v,visited, stack)

        print("final",stack)


newGraph = Graph()
newGraph.addEdge("A","C")
newGraph.addEdge("C","E")
newGraph.addEdge("E","H")
newGraph.addEdge("E","F")
newGraph.addEdge("F","G")
newGraph.addEdge("B","D")
newGraph.addEdge("B","D")
newGraph.addEdge("B","D")


print("Graph keys",newGraph)
newGraph.topologicSort()
