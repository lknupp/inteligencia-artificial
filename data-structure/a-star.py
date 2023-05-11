from utils import generate_weighted_graph, validate_path, initialize_graph, calculate_euclidian_distance, pathway_recursive, relax
from node import Node
import time
import random
import queue

from status import Status


def main():
    graph_nodes: int = 5000
    graph: list[Node] = generate_weighted_graph(graph_nodes, 10)
    print(f'Nodes number: {graph_nodes}')
    source: Node = graph[random.randint(0, len(graph) - 1)]
    destination: Node = graph[random.randint(0, len(graph) - 1)]

    print(f'First city: {source.name}')
    print(f'Last city: {destination.name}')
    initial_time: float = time.perf_counter()
    initialize_graph(graph)
    a_star(source, destination)
    validate_path(pathway_recursive(destination), source, destination)
    end_time: float = time.perf_counter()
    print(f'Time elapsed: {(end_time - initial_time):.2f} seconds')


def a_star(source: Node, destination: Node):
    """
    Executes the A* algorithm to find the shortest path between the source and destination nodes in a graph.

    Args:
        source: The source node.
        destination: The destination node.
    """
    p_queue: queue.PriorityQueue = queue.PriorityQueue()
    p_queue.put((0, source))
    source.estimated_cost = 0
    source.father_node = source
    node: Node
    while not p_queue.empty():
        _, node = p_queue.get()
        node.status = Status.VISITED

        if node == destination:
            break
        for edge in node.adjacency_list:
            relax(node, edge.node, edge.weight)
            if edge.node.status == Status.NOT_VISITED:
                weight: float = edge.node.estimated_cost + \
                    calculate_euclidian_distance(
                        node.coordinate, edge.node.coordinate)
                p_queue.put((weight, edge.node))


if __name__ == '__main__':
    main()
