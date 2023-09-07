# Algorithms
# BFS - breadth first
# DFS - depth first

'''
- Define Graph. Graph is key value pair. Key is vertex. Values are list of edges.
- Add function to add edge to key / vertex.
- BFS: Level order Traversal Search -- FIFO
    Add search element to visited list and a queue (FIFO)
    Start Empty path List
    While Queue For loop to find edges of pop(0) first element in queue
    Add popped element to Path
    if edge is not in Visited then add in visited and also in queue
    return Path
- DFS: Node traversal Search -- LIFO
    Add search element to visited list and a Stack (LIFO)
    Start Empty path List
    While Stack For loop to find edges of pop last element in stack
    Add popped element to Path
    if edge is not in Visited then add in visited and also in stack
    return Path
'''

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

    # depth first traversal 
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