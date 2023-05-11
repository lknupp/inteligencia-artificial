import unittest
import bfs
import dijkstra
import node
import coordinate
import status


class TestBfs(unittest.TestCase):

    def test_bfs(self):
        graph: list = [[2, 6], [1, 3, 4], [2, 5], [
            2, 5, 6], [3, 4, 8], [1, 4, 7], [6, 8], [5, 7]]
        self.assertEqual(bfs.bfs(graph, 0, 7), [-2, 0, 1, 1, 2, 0, 5, 6])
        self.assertEqual(bfs.bfs(graph, 0, 8), [-2, 0, 1, 1, 2, 0, 5, 6])

    def test_path(self):
        self.assertEqual(bfs.pathway(
            [-2, 0, 1, 1, 2, 0, 5, 6], 7), [1, 6, 7, 8])


class TestDijkstra(unittest.TestLoader):
    node1: node.Node = node.Node(
        0, status.Status.NOT_VISITED, coordinate.Coordinate(1, 1))
    node2: node.Node = node.Node(
        1, status.Status.NOT_VISITED, coordinate.Coordinate(1, 1))
    node3: node.Node = node.Node(
        2, status.Status.NOT_VISITED, coordinate.Coordinate(1, 1))
    node4: node.Node = node.Node(
        3, status.Status.NOT_VISITED, coordinate.Coordinate(1, 1))
    node5: node.Node = node.Node(
        4, status.Status.NOT_VISITED, coordinate.Coordinate(1, 1))
    node1.adjacency_list = [node.Edge(node2, 8), node.Edge(node3, 5)]
    node2.adjacency_list = [node.Edge(node5, 2), node.Edge(node4, 1)]
    node3.adjacency_list = [node.Edge(node5, 12), node.Edge(node4, 5)]
    node4.adjacency_list = [node.Edge(node5, 5)]
    node5.adjacency_list = [node.Edge(node3, 12)]

    graph: list[node.Node] = [node1, node2, node3, node4, node5]
    source: int = 0
    destination: int = 4
    dijkstra.dijkstra(graph, source, destination)
    print(dijkstra.pathway_recursive(graph[destination]))


if __name__ == '__main__':
    unittest.main()
