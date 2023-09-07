import sys

def dijkstra(graph, start_node):
    # Initialize distances dictionary with infinity distance for all nodes except the start node
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0

    # Initialize visited set to keep track of visited nodes
    visited = set()

    # Initialize dictionary to track the shortest path
    path = {node: [] for node in graph}

    while visited != set(graph):
        # Find the node with the minimum distance from the set of unvisited nodes
        min_node = min((node for node in graph if node not in visited), key=lambda n: distances[n])

        # Mark the current node as visited
        visited.add(min_node)

        # Update distances of neighboring nodes and track the shortest path
        for neighbor, weight in graph[min_node].items():
            if distances[min_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[min_node] + weight
                path[neighbor] = path[min_node] + [neighbor]

    return distances, path


# Example usage
graph = {
    'A': {'B': 3, 'C': 2},
    'B': {'A': 3, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 2},
    'D': {'B': 5, 'C': 2}
}

start_node = 'A'
distances, shortest_path = dijkstra(graph, start_node)

# Print the shortest distances from the start node to all other nodes
for node, distance in distances.items():
    print(f"Shortest distance from {start_node} to {node}: {distance}")
    print(f"Shortest path: {start_node} -> {' -> '.join(shortest_path[node])}")
    print()