import networkx as nx
import matplotlib.pyplot as plt

# Create a graph with U-Bahn stations in Hamburg
G = nx.Graph()

# U-Bahn line 2 stations
stations_line_2 = ['Messehallen', 'Gänsemarkt', 'Jungfernstieg', "Hauptbahnhof Nord", "Berliner Tor", "Burgstraße", "Hammer Kirche", "Rauhes Haus", "Horner Rennbahn"]
stations_line_3 = ["Saarlandstraße","Kellinghusestraße","Schlump","Sternschanze","Feldstraße", 'St. Pauli', 'Landungsbrücken', 'Baumwall', "Rödingsmarket", "Rathaus", "Mönckebergerstraße", "Hauptbahnhof Süd", "Berliner Tor", "Lübecker Straße", "Uhlandstraße", "Mundsburg", "Hamburger Straße", "Barmbek"]

G.add_nodes_from(stations_line_2)
G.add_nodes_from(stations_line_3)

# U-Bahn line 2 connections
G.add_edges_from([('Messehallen', 'Gänsemarkt'), ('Gänsemarkt', 'Jungfernstieg'), ("Jungfernstieg", "Hauptbahnhof Nord"),
                  ("Hauptbahnhof Nord", "Berliner Tor"), ("Berliner Tor", "Burgstraße"), ("Burgstraße", "Hammer Kirche"),
                  ("Hammer Kirche", "Rauhes Haus"), ("Rauhes Haus", "Horner Rennbahn")])

# U-Bahn line 3 connections
G.add_edges_from([("Saarlandstraße","Kellinghusestraße"), ("Kellinghusestraße","Schlump"), ("Schlump","Sternschanze"),
                  ("Sternschanze","Feldstraße"), ("Feldstraße", 'St. Pauli'), ('St. Pauli', 'Landungsbrücken'), 
                  ('Landungsbrücken', 'Baumwall'), ("Baumwall","Rödingsmarket"), ("Rödingsmarket", "Rathaus"), 
                  ("Rathaus", "Jungfernstieg"),("Rathaus", "Mönckebergerstraße"), ("Mönckebergerstraße", "Hauptbahnhof Süd"),
                  ("Hauptbahnhof Süd", "Berliner Tor"), ("Berliner Tor", "Lübecker Straße"), ("Lübecker Straße", "Uhlandstraße"),
                  ("Uhlandstraße", "Mundsburg"), ("Mundsburg", "Hamburger Straße"), ("Hamburger Straße", "Barmbek"),
                  ("Barmbek", "Saarlandstraße")])
# Visualize the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=8)
plt.title("Transport Network in Hamburg (U-Bahn lines 2 and 3)")
plt.show()

