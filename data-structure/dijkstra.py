from utils import generate_weighted_graph, validate_path
from node import Node
import time
import random
import queue

from status import Status


def main():
    graph_nodes: int = 20
    graph: list[Node] = generate_weighted_graph(10000, 10)
    print(f'Nodes number: {graph_nodes}')
    idx: int = random.randint(0, len(graph) - 1)
    aim: int = random.randint(0, len(graph) - 1)

    print(f'First city: {idx + 1}')
    print(f'Last city: {aim + 1}')
    initial_time: float = time.perf_counter()
    dijkstra(graph, idx, aim)
    validate_path(pathway_recursive(graph[aim]), idx, aim)
    end_time: float = time.perf_counter()
    print(f'Time elapsed: {(end_time - initial_time):.2f} seconds')


def dijkstra(graph: list[Node], source: int, destination: int):
    p_queue: queue.PriorityQueue = queue.PriorityQueue()
    node: Node = graph[source]
    p_queue.put((0, node))
    node.status = Status.PROCESSING
    node.estimated_cost = 0
    node.father_node = node
    while not p_queue.empty():
        _, node = p_queue.get()
        node.status = Status.VISITED

        if node == graph[destination]:
            break
        for edge in node.adjacency_list:
            relax(node, edge.node, edge.weight)
            if edge.node.status != Status.VISITED:
                edge.node.status = Status.PROCESSING
                p_queue.put((edge.node.estimated_cost, edge.node))


def pathway_recursive(node: Node, path: list = []) -> list:
    if node.father_node == node:
        path.append(node.id + 1)
        return path
    elif node.father_node == None:
        return path
    pathway_recursive(node.father_node, path)
    path.append(node.id + 1)
    return path


def relax(cur_node: Node, next_node: Node, weight: int) -> None:
    if (next_node.estimated_cost > (cur_node.estimated_cost + weight)):
        next_node.estimated_cost = cur_node.estimated_cost + weight
        next_node.father_node = cur_node


if __name__ == '__main__':
    main()
