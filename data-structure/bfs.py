from utils import generate_weighted_graph, validate_path, initialize_graph, pathway_recursive
from node import Node
import time
import random
import queue

from status import Status


def main():
    graph_nodes: int = 6000
    graph: list[Node] = generate_weighted_graph(graph_nodes, 20)
    print(f'Nodes number: {len(graph)}')
    initial_time: float = time.perf_counter()
    source: Node = graph[random.randint(0, len(graph) - 1)]
    destination: Node = graph[random.randint(0, len(graph) - 1)]

    print(f'First city: {source.name}')
    print(f'Last city: {destination.name}')
    bfs(graph, source, destination)
    validate_path(pathway_recursive(destination), source, destination)
    end_time: float = time.perf_counter()
    print(f'Time elapsed: {(end_time - initial_time):.2f} seconds')


def bfs(graph: list[Node], source: Node, destination: Node) -> None:
    initialize_graph(graph)
    node: Node = source
    node.father_node = node
    q: queue.Queue = queue.Queue()
    q.put(node)
    while not q.empty():
        node = q.get()
        node.status = Status.VISITED
        if destination == node:
            break
        for edge in node.adjacency_list:
            if edge.node.status == Status.NOT_VISITED:
                edge.node.status = Status.PROCESSING
                edge.node.father_node = node
                q.put(edge.node)


def pathway(father: list, aim: int) -> list:
    path: list = []
    idx: int = aim
    if father[idx] != -1:
        path.append(idx + 1)
        try:
            while father[idx] != -2:
                idx = father[idx]
                path.append(idx + 1)
        except IndexError:
            return []
        path.reverse()
    return path


if __name__ == '__main__':
    main()
