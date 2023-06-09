from utils import generate_weighted_graph, validate_path, initialize_graph, pathway_recursive, relax
from node import Node
import time
import random
import queue

from status import Status


def main():
    graph_nodes: int = 5000
    graph: list[Node] = generate_weighted_graph(graph_nodes, 10)
    print(f'Nodes number: {len(graph)}')
    source: Node = graph[random.randint(0, len(graph) - 1)]
    destination: Node = graph[random.randint(0, len(graph) - 1)]

    print(f'First city: {source.name}')
    print(f'Last city: {destination.name}')
    initial_time: float = time.perf_counter()
    initialize_graph(graph)
    dijkstra(source, destination)
    validate_path(pathway_recursive(destination), source, destination)
    end_time: float = time.perf_counter()
    print(f'Time elapsed: {(end_time - initial_time):.2f} seconds')


def dijkstra(source: Node, destination: Node):
    """
    Performs Dijkstra's algorithm to find the shortest path in a weighted graph.

    Args:
        source: The source node to start the search from.
        destination: The destination node to reach.

    """
    p_queue: queue.PriorityQueue = queue.PriorityQueue()
    node: Node = source
    p_queue.put((0, node))
    node.estimated_cost = 0
    node.father_node = node
    while not p_queue.empty():
        _, node = p_queue.get()
        node.status = Status.VISITED

        if node == destination:
            break
        for edge in node.adjacency_list:
            relax(node, edge.node, edge.weight)
            if edge.node.status != Status.VISITED:
                edge.node.status = Status.PROCESSING
                p_queue.put((edge.node.estimated_cost, edge.node))


if __name__ == '__main__':
    main()
