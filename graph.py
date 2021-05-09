import networkx as nx
import matplotlib.pyplot as plt


def create_graph():
    G = nx.Graph()
    f = open('input.txt')
    n = int(f.readline())
    for i in range(n):
        graph_edge_list = f.readline().split()
        G.add_edge(int(graph_edge_list[0]), int(graph_edge_list[1]))
    return G


def welsh_powell(G):
    node_list = sorted(G.nodes(), key=lambda x: list(G.neighbors(x)))
    col_val = {}
    col_val[node_list[0]] = 0
    for node in node_list[1:]:
        available = [True] * len(G.nodes())
        for adj_node in G.neighbors(node):
            if adj_node in col_val.keys():
                col = col_val[adj_node]
                available[col] = False
        clr = 0
        for clr in range(len(available)):
            if available[clr]:
                break
        col_val[node] = clr
    return col_val


def assign_color(value):
    if value == 0:
        return '#ed5858'
    if value == 1:
        return '#edcf58'
    if value == 2:
        return '#99ed58'
    if value == 3:
        return '#58eded'
    if value == 4:
        return '#5aa4ed'
    if value == 5:
        return '#665aed'
    if value == 6:
        return '#c258e8'


def draw_graph(G, col_val):
    pos = nx.spring_layout(G)
    color_map = []
    for node in G.nodes():
        color_map.append(assign_color(col_val.get(node, 0)))
    nx.draw(G, pos, with_labels=True, node_color=color_map,
            edge_color='black', width=1)
