import random
import utils
import time


def main():
    graph: list = utils.generate_graph()
    print(f'Nodes number: {len(graph)}')
    initial_time: float = time.perf_counter()
    idx: int = random.randint(0, len(graph) - 1)
    aim: int = random.randint(0, len(graph) - 1)
    print(f'First city: {idx + 1}')

    print(f'Last city: {aim + 1}')
    path: list = dfs(graph, idx, aim, [False]*len(graph))

    if len(path):
        print(' -> '.join([str(city) for city in path]))
    else:
        print(f'There is no path from city {idx + 1} to {aim + 1}')
    end_time: float = time.perf_counter()
    print(f'Time elapsed: {(end_time - initial_time):.2f} seconds')


def dfs(graph: list, idx: int, aim: int, visited: list) -> list:
    if idx >= len(graph):
        return []
    if visited[idx]:
        return []

    visited[idx] = True

    if idx == aim:
        return [idx + 1]
    for node in graph[idx]:
        path: list = dfs(graph, node, aim, visited)
        if path:
            return [idx + 1] + path
    return []


if __name__ == '__main__':
    main()
