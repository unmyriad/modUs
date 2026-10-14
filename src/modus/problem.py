import networkx as nx

def generate_graph(num_nodes, degree, seed):
    if (num_nodes * degree) % 2 != 0:
        raise ValueError("num_nodes and degree must be even")
    G = nx.random_regular_graph(n=num_nodes, d=degree, seed=seed)
    return G

print(generate_graph(80, 4, 42))
