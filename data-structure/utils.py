import random
from node import Node, Edge
from coordinate import Coordinate
from status import Status
from math import sqrt, floor, inf


def generate_graph() -> list:
    """
    Generates a directed and non-simple graph with at least 100 nodes and a 
    maximum of 10000 nodes.
    """
    graph_nodes: int = random.randint(100, 10000)
    graph: list = [0] * graph_nodes
    for i in range(graph_nodes):
        graph[i] = random.sample(
            range(1, graph_nodes), random.randint(1, max(1, graph_nodes // 1000)))
    return graph


def print_adjacency_list(graph: list) -> None:
    for adjacency_list in graph:
        print('[', f', '.join([str(node) for node in adjacency_list]), '],')

    return


def generate_weighted_graph(nodes_number: int, max_nodes_connections: int) -> list:
    nodes_number, max_nodes_connections = validate_nodes_number(
        nodes_number, max_nodes_connections)
    graph_nodes: int = nodes_number
    coordinates: list[Coordinate] = generate_coordinate_list(graph_nodes)
    weighted_graph: list = [
        Node(id, Status.NOT_VISITED, coordinates[id]) for id in range(graph_nodes)]
    node: Node
    for i, node in enumerate(weighted_graph):
        tmp_padjacency_list: list[Edge] = list()
        for j in create_adjacency_list(i, graph_nodes, random.randint(1, max_nodes_connections)):
            adj_node: Node = weighted_graph[j]
            min_weight: int = floor(calculate_euclidian_distance(
                node.coordinate, adj_node.coordinate))
            weight: int = random.randint(min_weight, max(min_weight * 2, 100))
            edge: Edge = Edge(adj_node, weight)
            tmp_padjacency_list.append(edge)
        node.adjacency_list = tmp_padjacency_list
    return weighted_graph


def validate_nodes_number(nodes_number: int, max_nodes_connections: int) -> tuple:
    default_nodes_value: int = 10
    if nodes_number <= 0:
        nodes_number = default_nodes_value
        print(
            f'The number of nodes was set to the default value of {nodes_number}')
    if max_nodes_connections > nodes_number:
        max_nodes_connections = max(1, nodes_number // 5)
        print(
            f'The maximum number of connections was set to the maximum of{max_nodes_connections}')

    return nodes_number, max_nodes_connections


def create_adjacency_list(node_id: int, nodes_number: int, edges_number: int) -> list:
    counts: list = [
        1 if i != node_id else 0 for i in range(0, nodes_number)]

    adjacency_list: list = random.sample(
        range(0, nodes_number), random.randint(1, edges_number), counts=counts)

    return adjacency_list


def generate_coordinate_list(quantity: int) -> list[Coordinate]:
    tmp_coordinates: set = set()
    while len(tmp_coordinates) != quantity:
        tmp_coordinates.add(generate_coordinate(min_coordinate=-1 *
                                                quantity, max_coordinate=quantity))
    coordinates: list[Coordinate] = list()
    for i in tmp_coordinates:
        aux: Coordinate = Coordinate(i[0], i[1])
        coordinates.append(aux)
    return coordinates


def generate_coordinate(min_coordinate: int = -100, max_coordinate: int = 100):

    x_coordinate: int = random.randint(min_coordinate, max_coordinate)
    y_coordinate: int = random.randint(min_coordinate, max_coordinate)

    return x_coordinate, y_coordinate


def calculate_euclidian_distance(first_point: Coordinate, second_point: Coordinate) -> float:
    x_distance: int = abs(first_point.x_coordinate - second_point.x_coordinate)
    y_distance: int = abs(first_point.y_coordinate - second_point.y_coordinate)
    distance: float = sqrt(x_distance ** 2 + y_distance ** 2)

    return distance


def validate_path(path: list[int], source: int, destination: int) -> None:
    if len(path):
        print(' -> '.join([str(city) for city in path]))
    else:
        print(f'There is no path from city {source + 1} to {destination + 1}')


if __name__ == '__main__':
    # generate_weighted_graph(1000, 10)
    # print(calculate_euclidian_distance(Coordinate(-5, 2), Coordinate(-3, 4)))
    # node: Node
    # for node in generate_weighted_graph(10, 3):
    #     print(
    #         f'Status: {node.status} Coordinate: ({node.coordinate.x_coordinate},{node.coordinate.y_coordinate})')
    #     print(len(node.adjacency_list))
    #     for edge in node.adjacency_list:
    #         print(f'\tNode {edge.node} Weight: {edge.weight}')
    # print(generate_coordinate_list(10000))

    pass
