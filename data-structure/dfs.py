from utils import generate_weighted_graph, validate_path, initialize_graph, pathway_recursive
from node import Node
import time
import random

from status import Status


def main():
    graph_nodes: int = 1000
    graph: list[Node] = generate_weighted_graph(graph_nodes, 10)
    print(f'Nodes number: {len(graph)}')
    initial_time: float = time.perf_counter()
    source: Node = graph[random.randint(0, len(graph) - 1)]
    destination: Node = graph[random.randint(0, len(graph) - 1)]

    print(f'First city: {source.name}')
    print(f'Last city: {destination.name}')
    initialize_graph(graph)
    dfs(source, source, destination)
    validate_path(pathway_recursive(destination), source, destination)
    end_time: float = time.perf_counter()
    print(f'Time elapsed: {(end_time - initial_time):.2f} seconds')


def dfs(cur_node: Node, prev_node: Node, destination: Node) -> bool:
    """
    Performs depth-first search (DFS) algorithm on the graph recursively.

    Args:
        cur_node: The current node being visited.
        prev_node: The previous node visited.
        destination: The destination node to reach.

    Returns:
        bool: True if the destination is reached, False otherwise.
    """
    if cur_node == destination:
        cur_node.father_node = prev_node
        return True
    if cur_node.status == Status.VISITED:
        return False
    cur_node.status = Status.VISITED

    for edge in cur_node.adjacency_list:
        found: bool = dfs(edge.node, cur_node, destination)
        if found:
            cur_node.father_node = prev_node
            return True

    return False


if __name__ == '__main__':
    main()
