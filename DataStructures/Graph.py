# Define Graph using adjacency list
class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    
    # breadth first traversal - level order traversal
    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        path = []
        while queue:
            deVertex = queue.pop(0)  # Note first in first out
            path.append(deVertex)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)
        return "->".join(path)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        path  = []
        while stack:
            popVertex = stack.pop() # Note last in first out
            path.append(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)
        return "->".join(path)    

customDict = { "a" : ["b","c"],
            "b" : ["a", "d", "e"],
            "c" : ["a", "e"],
            "d" : ["b", "e", "f"],
            "e" : ["d", "f", "c"],
            "f" : ["d", "e"]
               }


g = Graph(customDict)
print(g.bfs("a"))
print(g.dfs("a"))