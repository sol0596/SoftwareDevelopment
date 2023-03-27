import matplotlib.pyplot as plt
import networkx as nx

import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.graph["Treasure Collection"] = "Path Finders & Map Readers"


G.add_edges_from([
    ("Leeds", "London", {"Weight": 0.1}),
    ("Leeds", "Monrovia", {"Weight": 0.1}),
    ("Monrovia", "Warsaw", {"Weight":0.2}),
    ("Monrovia", "Madrid", {"Weight":0.6}),
    ("London", "Paris",{"Weight":1}),
    ("London", "New York",{"Weight": 1}),
    ("Madrid", "Tirana", {"Weight":1}),
    ("Madrid", "Rome", {"Weight":1}),
    ("Paris", "Islamabad", {"Weight":0.1}),
    ("Paris", "Berlin", {"Weight":0.1}),
    ("New York", "Tokyo", {"Weight":0.1}),
    ("New York", "Washington DC", {"Weight":0.1})

])
pos={
    "Leeds":(22,52),
    "London":(33, 30),
    "Monrovia":(8, 40),
    "Warsaw":(12.6, 23),
    "Madrid":(0.1, 23),
    "Paris":(26, 17),
    "New York":(40, 17),
    "Tirana":(-5, 16),
    "Rome":(5, 17),
    "Islamabad":(20, 11),
    "Berlin":(30, 11),
    "Tokyo":(36, 11),
    "Washington DC":(46, 14)
}

edge_labels = {(u, v):d["Weight"] for u,v,d in G.edges(data=True)}

nx.draw(G, pos=pos, with_labels=True,
        node_color = "blue", node_size = 1000,
        font_color = "black", font_size = 8, font_family = "Arial", font_weight = "bold",
        edge_color = "blue",
        width = 1
)

nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, label_pos=0.5)



plt.margins(0.2)
plt.show()