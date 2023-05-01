import random


def generate_graph() -> list:
    """
    Generates a directed and non-simple graph with at least 5 nodes and a 
    maximum of 15 nodes.
    """
    graph_nodes: int = random.randint(100, 10000)
    graph: list = [0] * graph_nodes
    for i in range(graph_nodes):
        graph[i] = random.sample(
            range(1, graph_nodes), random.randint(1, max(1, graph_nodes // 1000)))
    return graph


def print_adjacency_list(graph: list) -> None:
    for adjacency_list in graph:
        print('[', f', '.join([str(node) for node in adjacency_list]), '],')

    return


if __name__ == '__main__':
    generate_graph()
