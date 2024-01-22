import networkx as nx
import osmnx as ox  
import requests
import matplotlib.cm as cm
import matplotlib.colors as colors

ox.config(use_cache=True, log_console=True)
ox.__version__

G = ox.graph_from_place('속초시, 강원도, 대한민국', network_type = 'drive')
fig, ax = ox.plot_graph(G)

G_proj = ox.project_graph(G)
nodes_proj = ox.graph_to_gdfs(G_proj, edges=False)
graph_area_m = nodes_proj.unary_union.convex_hull.area
print(graph_area_m)

stats = ox.stats.basic_stats(G_proj, 
                       area=graph_area_m)

stats

#more_stats = ox.extended_stats(G, ecc=True, bc=True, cc=True) 
for key in sorted(stats.keys()):
    print(key)
#more_stats['degree_centrality_avg']


edge_centrality = nx.closeness_centrality(nx.line_graph(G))
nx.set_edge_attributes(G, edge_centrality, 'edge_centrality')

ec = ox.plot.get_edge_colors_by_attr(G, 'edge_centrality', cmap='inferno')
fig, ax = ox.plot_graph(G, edge_color=ec, edge_linewidth=2, node_size=0)