import unittest
import bfs


class TestBfs(unittest.TestCase):

    def test_bfs(self):
        graph: list = [[2, 6], [1, 3, 4], [2, 5], [
            2, 5, 6], [3, 4, 8], [1, 4, 7], [6, 8], [5, 7]]
        self.assertEqual(bfs.bfs(graph, 0, 7), [-2, 0, 1, 1, 2, 0, 5, 6])
        self.assertEqual(bfs.bfs(graph, 0, 8), [-2, 0, 1, 1, 2, 0, 5, 6])

    def test_path(self):
        self.assertEqual(bfs.pathway(
            [-2, 0, 1, 1, 2, 0, 5, 6], 7), [1, 6, 7, 8])


if __name__ == '__main__':
    unittest.main()
