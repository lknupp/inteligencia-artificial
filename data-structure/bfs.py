import random
import queue
import time
from utils import generate_graph, print_adjacency_list


def main():
    graph: list = generate_graph()
    print(f'Nodes number: {len(graph)}')
    initial_time: float = time.perf_counter()
    idx: int = random.randint(0, len(graph) - 1)
    aim: int = random.randint(0, len(graph) - 1)

    print(f'First city: {idx + 1}')
    print(f'Last city: {aim + 1}')
    bfs_tree: list = bfs(graph, idx, aim)
    path: list = pathway(bfs_tree, aim)
    if len(path):
        print(' -> '.join([str(city) for city in path]))
    else:
        print(f'There is no path from city {idx + 1} to {aim + 1}')
    end_time: float = time.perf_counter()
    print(f'Time elapsed: {(end_time - initial_time):.2f} seconds')


def bfs(graph: list, idx: int, aim: int) -> list:
    visited: list = [False] * len(graph)
    father: list = [-1] * len(graph)
    father[idx] = -2
    q: queue.Queue = queue.Queue()
    q.put(idx)
    while not q.empty():
        node = q.get()
        visited[node] = True
        if aim == node:
            break
        for vertex in graph[node]:
            vertex = vertex - 1
            if visited[vertex] == False:
                visited[vertex] = True
                father[vertex] = node
                q.put(vertex)
    return father


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


def pathway_recursive(father: list, aim: int, path: list = []) -> list:
    if father[aim] == -2:
        path.append(aim + 1)
        return path
    elif father[aim] == -1:
        return path
    pathway_recursive(father, father[aim], path)
    path.append(aim + 1)
    return path


if __name__ == '__main__':
    main()
