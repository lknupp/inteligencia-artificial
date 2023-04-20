import random


def main():
    graph: list = [[2, 6], [1, 3, 4], [2, 5], [
        2, 5, 6], [3, 4, 8], [1, 4, 7], [6, 8], [5, 7]]

    idx: int = random.randint(0, len(graph) - 1)
    # aim: int = random.randint(0, len(graph) - 1)
    aim: int = 10
    print(f'First city: {idx + 1}')

    print(f'Last city: {aim + 1}')
    path: list = dfs(graph, idx, aim, [False]*len(graph))

    if len(path):
        print(' -> '.join([str(city) for city in path]))
    else:
        print(f'There is no path from city {idx + 1} to {aim + 1}')


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
