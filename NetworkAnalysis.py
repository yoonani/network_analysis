import networkx as nx
import matplotlib.pyplot as plt 

# Empty Graph
g = nx.Graph()

type( g )

# add node
g.add_nodes_from([1, 2, 3, 4, 5, 6] )
# for add each node : g.add_node(1)

# add edge
g.add_edges_from( [
    (1, 3), (2, 4), (2, 5), (2, 6), (3, 4), (4, 6), (5, 6)
] )
# for add each edge : g.add_edge(1, 3)

print( g.nodes() )
print( g.edges() )
print( g.number_of_nodes() )
print( g.number_of_edges() )


# network visualization
nx.draw_networkx( g )
plt.axis( 'off' )
plt.show( )