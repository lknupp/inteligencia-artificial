from status import Status
from coordinate import Coordinate
from dataclasses import dataclass
from math import inf


class Node:
    def __init__(self, id: int, name: str, status: Status, coordinate: Coordinate) -> None:
        """
        Initializes a Node object.

        Args:
            id: The unique identifier for the node.
            name: The name or label of the node.
            status: The status of the node.
            coordinate: The coordinate of the node.

        """
        self.id: int = id
        self.name: str = name
        self.status: Status = status
        self.discovery_time: int
        self.finish_time: int
        self.father_node: Node = None
        self.coordinate: Coordinate = coordinate
        self.estimated_cost: int = inf
        self.adjacency_list: list['Edge'] = list()

    def __lt__(self, other: 'Node'):
        """
        Less than comparison method based on estimated cost.

        Args:
            other: The other Node object to compare against.

        Returns:
            bool: True if the estimated cost of self is less than other, False otherwise.
        """
        return self.estimated_cost < other.estimated_cost

    def add_node(self, node: 'Node') -> None:
        self.adjacency_list.append(node)


@dataclass
class Edge:
    node: Node
    weight: int
