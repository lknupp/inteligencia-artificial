import random
import queue


def main():
    # graph: list = [[2, 3], [1, 3, 4], [2, 4, 5], [2, 3, 5, 6], [3, 4], [4]]
    graph: list = [[2, 6], [1, 3, 4], [2, 5], [
        2, 5, 6], [3, 4, 8], [1, 4, 7], [6, 8], [5, 7]]

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


def bfs(graph: list, idx: int, aim: int) -> list:
    visited: list = [False] * len(graph)
    father: list = [-1] * len(graph)

    q: queue.Queue = queue.Queue()
    q.put(idx)
    while not q.empty():
        node = q.get()
        if aim == node:
            break
        for vertex in graph[node]:
            vertex = vertex - 1
            if visited[vertex] == False:
                visited[vertex] = True
                father[vertex] = node
                q.put(vertex)
        visited[node] = True

    return father


def pathway(father: list, aim: int) -> list:
    path: list = [aim + 1]
    idx: int = aim
    try:
        while father[idx] != -1:
            idx = father[idx]
            path.append(idx + 1)
    except IndexError:
        return []
    path.reverse()
    return path


def pathway_recursive(father: list, aim: int, path: list = []) -> list:
    if father[aim] == -1:
        path.append(aim + 1)
        return path
    pathway_recursive(father, father[aim], path)
    path.append(aim + 1)
    return path


if __name__ == '__main__':
    main()
