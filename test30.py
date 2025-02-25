import networkx as nx
import matplotlib.pyplot as plt
network = nx.Graph()
color_list = ["gold", "red", "violet","green","blue"]
plt.figure(figsize=(8, 6))
plt.title('Example of Graph Representation', size=10)

network.add_nodes_from([1,2,3,4,5])
network.add_edge(1,5)
network.add_edge(2,4)
network.add_edge(3,3)
network.add_edge(4,2)
network.add_edge(5,1)
print(f"This network has now {network.number_of_nodes()} nodes.")

nx.draw_networkx(network,node_color=color_list, with_labels=True)

plt.show()