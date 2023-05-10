from status import Status
from coordinate import Coordinate
from dataclasses import dataclass
from math import inf


class Node:
    def __init__(self, id: int, status: Status, coordinate: Coordinate) -> None:
        self.id: int = id
        self.status: Status = status
        self.discovery_time: int
        self.finish_time: int
        self.father_node: Node = None
        self.coordinate: Coordinate = coordinate
        self.estimated_cost: int = inf
        self.adjacency_list: list['Edge'] = list()

    def __lt__(self, other: 'Node'):
        return self.estimated_cost < other.estimated_cost

    def add_node(self, node: 'Node') -> None:
        self.adjacency_list.append(node)


@dataclass
class Edge:
    node: Node
    weight: int
