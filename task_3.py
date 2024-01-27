import networkx as nx
import heapq

# Create a graph with U-Bahn stations in Hamburg
G = nx.Graph()

# U-Bahn line 2 stations
stations_line_2 = ['Messehallen', 'Gänsemarkt', 'Jungfernstieg', "Hauptbahnhof Nord", "Berliner Tor", "Burgstraße", "Hammer Kirche", "Rauhes Haus", "Horner Rennbahn"]
stations_line_3 = ["Saarlandstraße","Kellinghusestraße","Schlump","Sternschanze","Feldstraße", 'St. Pauli', 'Landungsbrücken', 'Baumwall', "Rödingsmarket", "Rathaus", "Mönckebergerstraße", "Hauptbahnhof Süd", "Berliner Tor", "Lübecker Straße", "Uhlandstraße", "Mundsburg", "Hamburger Straße", "Barmbek"]

G.add_nodes_from(stations_line_2)
G.add_nodes_from(stations_line_3)

# U-Bahn line 2 connections with weights
G.add_edges_from([('Messehallen', 'Gänsemarkt', {'weight': 1}),
                  ('Gänsemarkt', 'Jungfernstieg', {'weight': 1}),
                  ("Jungfernstieg", "Hauptbahnhof Nord", {'weight': 2}),
                  ("Hauptbahnhof Nord", "Berliner Tor", {'weight': 1}),
                  ("Berliner Tor", "Burgstraße", {'weight': 1}),
                  ("Burgstraße", "Hammer Kirche", {'weight': 2}),
                  ("Hammer Kirche", "Rauhes Haus", {'weight': 1}),
                  ("Rauhes Haus", "Horner Rennbahn", {'weight': 1})])

# U-Bahn line 3 connections with weights
G.add_edges_from([("Saarlandstraße","Kellinghusestraße", {'weight': 3}),
                  ("Kellinghusestraße","Schlump", {'weight': 1}),
                  ("Schlump","Sternschanze", {'weight': 2}),
                  ("Sternschanze","Feldstraße", {'weight': 1}),
                  ("Feldstraße", 'St. Pauli', {'weight': 1}),
                  ('St. Pauli', 'Landungsbrücken', {'weight': 1}),
                  ('Landungsbrücken', 'Baumwall', {'weight': 1}),
                  ("Baumwall","Rödingsmarket", {'weight': 2}),
                  ("Rödingsmarket", "Rathaus", {'weight': 1}),
                  ("Rathaus", "Jungfernstieg", {'weight': 1}),
                  ("Rathaus", "Mönckebergerstraße", {'weight': 1}),
                  ("Mönckebergerstraße", "Hauptbahnhof Süd", {'weight': 1}),
                  ("Hauptbahnhof Süd", "Berliner Tor", {'weight': 1}),
                  ("Berliner Tor", "Lübecker Straße", {'weight': 1}),
                  ("Lübecker Straße", "Uhlandstraße", {'weight': 2}),
                  ("Uhlandstraße", "Mundsburg", {'weight': 1}),
                  ("Mundsburg", "Hamburger Straße", {'weight': 1}),
                  ("Hamburger Straße", "Barmbek", {'weight': 1}),
                  ("Barmbek", "Saarlandstraße", {'weight': 2})])

# Dijkstra's algorithm to find the shortest path from a source to all other nodes
def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight['weight']

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Find shortest paths for all nodes
all_shortest_paths = {}

for start_node in G.nodes:
    shortest_distances = dijkstra(G, start_node)
    all_shortest_paths[start_node] = shortest_distances

# Print the shortest paths
print(all_shortest_paths)

