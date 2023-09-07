# Algorithm
# Dijkstra's Algorithm
# Find Shorted path in a weighted graph 

'''
Start with Given Node and find cost of moving to adjacent Nodes. 
Continue till end of all nodes.

# Define Graph - Set of Nodes, Edges Dict, Distances Dict
# Loop through Nodes to find min node in visited - remove when found
# Loop through edges of visited node and update weight
# finally visited nodes with min weight and Path showing adjacent node to every node
# for shortest path

'''

from collections import defaultdict

# Define graph
class Graph:
    def __init__(self):
        self.nodes = set()   # List of Nodes
        self.edges = defaultdict(list)    # Dict of Edge and adjacent Edges
        self.distances = {}   # Distance between Edges
    
    def addNode(self,value):
        self.nodes.add(value)
    
    # Append list of adjacent nodes 
    # Entry of distance between 2 nodes as a combination
    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance

# Dijkstra's Algorithm
def dijkstra(graph, initial):
    visited = {initial : 0}     # Dict of Visited nodes with their Weight
    path = defaultdict(list)    # Dict of various Paths
    print(visited)
    print(path)

    nodes = set(graph.nodes)    # Nodes

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)
    
    return visited, path


# Define Graph - Nodes, Edges DictList, Distances Dict
# Loop through Nodes to find min node in visited - remove when found
# Loop through edges of visited node and update weight
# finally visited nodes with min weight and Path showing adjacent node to every node
# for shortest path

class Graph1:
    def __init__(self, ):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
    
    def addNode(self, value):
        self.nodes.add(value)

    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance

    def __str__(self):
        values = [e for e in list(self.edges)]
        return ",".join(values)

def dijkstra1(graph, initial):
    # Dict to keep visited nodes with their commulative weight
    visited = {initial : 0}
    path = defaultdict(list)
    nodes = set(graph.nodes)

    while nodes:

        # Loop to find minnode from a given node. 
        # Remove it from node list. calculate its weight
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node

        if minNode is None: break   # All nodes visited.

        nodes.remove(minNode)
        currWeight = visited[minNode]

        # loop to get adjacent nodes - edge of given node. Calculate weight to get to Edge.
        for edge in graph.edges[minNode]:
            weight = currWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)

    return {"visited":visited,"path":path}


def ssspDj(node, visited, path):
    pathlist = [node]
    weight = visited[node]
    while visited[node] != 0:
        node = path[node][0]
        pathlist.insert(0,node)

    print("->".join(pathlist))
    print("Cost of Path", weight)

customGraph = Graph1()
#customGraph = Graph()
customGraph.addNode("A")
customGraph.addNode("B")
customGraph.addNode("C")
customGraph.addNode("D")
customGraph.addNode("E")
customGraph.addNode("F")
customGraph.addNode("G")
customGraph.addEdge("A", "B", 2)
customGraph.addEdge("A", "C", 5)
customGraph.addEdge("B", "C", 8)
customGraph.addEdge("B", "D", 1)
customGraph.addEdge("B", "E", 3)
customGraph.addEdge("C", "F", 7)
customGraph.addEdge("D", "E", 4)
customGraph.addEdge("E", "G", 9)
customGraph.addEdge("F", "G", 7)

sspsdata = dijkstra1(customGraph, "A")
ssspDj("G", dict(sspsdata["visited"]),dict(sspsdata["path"]))
# print(sspsdata)

# See change the distance from d to e to 1 and from b to e to 6.
# then to get to e from a ,
# shortest path should be a b d e
# but your code is giving a b e