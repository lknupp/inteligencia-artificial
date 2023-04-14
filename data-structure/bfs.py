import random
import queue


def main():
    graph: list = [[2, 3], [1, 3, 4], [2, 4, 5], [2, 3, 5, 6], [3, 4], [4]]
    idx: int = random.randint(0, len(graph) - 1)
    aim: int = random.randint(0, len(graph) - 1)
    print(f'First city: {idx + 1}')

    print(f'Last city: {aim + 1}')
    bfs_tree: list = bfs(graph, idx, aim)
    path: list = [i + 1 for i in pathway(bfs_tree, aim)]
    print(' -> '.join([str(f) for f in path[::-1]]))


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
    path: list = [aim]
    idx: int = aim
    while father[idx] != -1:
        idx = father[idx]
        path.append(idx)

    return path


if __name__ == '__main__':
    main()
