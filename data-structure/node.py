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


@dataclass
class Edge:
    weight: int
    node: Node

    def __init__(self, node: Node, weight: int):
        self.node: Node = node
        self.weight: int = weight
