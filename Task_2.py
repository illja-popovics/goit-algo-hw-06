from task_1 import G


# Function to find paths using DFS
def dfs_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph.neighbors(start):
        if node not in path:
            new_paths = dfs_paths(graph, node, end, path)
            for p in new_paths:
                paths.append(p)
    return paths

# Function to find paths using BFS
def bfs_paths(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (node, path) = queue.pop(0)
        for next_node in graph.neighbors(node):
            if next_node not in path:
                new_path = path + [next_node]
                queue.append((next_node, new_path))
                if next_node == end:
                    return new_path
# Choose start and end nodes for path finding
start_station = 'Messehallen'
end_station = 'Barmbek'

# Find paths using DFS
dfs_result = dfs_paths(G, start_station, end_station)

# Find path using BFS
bfs_result = bfs_paths(G, start_station, end_station)

# Print and compare results
print("DFS Paths:", dfs_result)
print("BFS Path:", bfs_result)

# Explanation of paths
print("\nExplanation:")
print("DFS explores one branch of the graph as deeply as possible before backtracking, "
      "so it may find longer paths before shorter ones.")
print("BFS explores all neighbors of a node before moving on to their neighbors, "
      "so it often finds the shortest path first.")
