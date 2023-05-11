import random
from node import Node, Edge
from coordinate import Coordinate
from status import Status
from math import sqrt, floor, inf
from parse_xml import parse_xml

MAX_CITIES_NUMBER = 5572


def generate_graph() -> list:
    """
    Generates a directed and non-simple graph with at least 100 nodes and a 
    maximum of 10000 nodes.

    Returns:
        list: The generated graph.
    """
    graph_nodes: int = random.randint(100, 10000)
    graph: list = [0] * graph_nodes
    for i in range(graph_nodes):
        graph[i] = random.sample(
            range(1, graph_nodes), random.randint(1, max(1, graph_nodes // 1000)))
    return graph


def print_adjacency_list(graph: list) -> None:
    """
    Prints the adjacency list representation of a graph.

    Args:
        graph (list): The graph represented as an adjacency list.
    """
    for adjacency_list in graph:
        print('[', f', '.join([str(node) for node in adjacency_list]), '],')

    return


def generate_weighted_graph(nodes_number: int, max_nodes_connections: int) -> list[Node]:
    """
    Generates a weighted graph with the specified number of nodes and maximum number of connections.

    Args:
        nodes_number: The number of nodes in the graph.
        max_nodes_connections: The maximum number of connections each node can have.

    Returns:
        list: The generated weighted graph represented as a list of Node objects.
    """
    nodes_number, max_nodes_connections = validate_nodes_number(
        nodes_number, max_nodes_connections)
    graph_nodes: int = nodes_number
    coordinates: list[Coordinate] = generate_coordinate_list(graph_nodes)
    cities = random.sample(parse_xml(), nodes_number)
    weighted_graph: list = [
        Node(id, cities[id], Status.NOT_VISITED, coordinates[id]) for id in range(graph_nodes)]
    node: Node
    for i, node in enumerate(weighted_graph):
        for j in create_adjacency_list(i, graph_nodes, random.randint(1, max_nodes_connections)):
            adj_node: Node = weighted_graph[j]
            min_weight: int = floor(calculate_euclidian_distance(
                node.coordinate, adj_node.coordinate))
            weight: int = random.randint(min_weight, 2 * min_weight)
            edge: Edge = Edge(adj_node, weight)
            node.adjacency_list.append(edge)
    return weighted_graph


def validate_nodes_number(nodes_number: int, max_nodes_connections: int) -> tuple:
    """
    Validates the number of nodes and maximum number of connections for a graph.

    Args:
        nodes_number: The number of nodes.
        max_nodes_connections: The maximum number of connections.

    Returns:
        tuple: A tuple containing the validated values for nodes_number and max_nodes_connections.
    """
    default_nodes_value: int = 10
    if nodes_number <= 0:
        nodes_number = default_nodes_value
        print(
            f'The number of nodes was set to the default value of {nodes_number}')
    if nodes_number > MAX_CITIES_NUMBER:
        nodes_number = MAX_CITIES_NUMBER
        print(f'The number of nodes was set to the maximum of {nodes_number}')
    if max_nodes_connections > 50:
        max_nodes_connections = random.randint(10, 50)
        print(
            f'The maximum number of connections was set to the maximum of {max_nodes_connections}')

    return nodes_number, max_nodes_connections


def create_adjacency_list(node_id: int, nodes_number: int, edges_number: int) -> list:
    """
    Creates an adjacency list for a node in a graph.

    Args:
        node_id: The ID of the node.
        nodes_number: The total number of nodes in the graph.
        edges_number: The number of edges to create.

    Returns:
        list: The adjacency list for the node.
    """
    counts: list = [
        1 if i != node_id else 0 for i in range(0, nodes_number)]

    adjacency_list: list = random.sample(
        range(0, nodes_number), random.randint(1, edges_number), counts=counts)

    return adjacency_list


def generate_coordinate_list(quantity: int) -> list[Coordinate]:
    """
    Generates a list of coordinates.

    Args:
        quantity: The number of coordinates to generate.

    Returns:
        list: The list of generated coordinates.
    """
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
    """
    Generates a random coordinate.

    Args:
        min_coordinate: The minimum value for the coordinate.
        max_coordinate: The maximum value for the coordinate.

    Returns:
        tuple: The generated coordinate in the form (x_coordinate, y_coordinate).
    """
    x_coordinate: int = random.randint(min_coordinate, max_coordinate)
    y_coordinate: int = random.randint(min_coordinate, max_coordinate)

    return x_coordinate, y_coordinate


def calculate_euclidian_distance(first_point: Coordinate, second_point: Coordinate) -> float:
    """
    Calculates the Euclidean distance between two points.

    Args:
        first_point: The first point.
        second_point: The second point.

    Returns:
        float: The Euclidean distance between the two points.
    """
    x_distance: int = abs(first_point.x_coordinate - second_point.x_coordinate)
    y_distance: int = abs(first_point.y_coordinate - second_point.y_coordinate)
    distance: float = sqrt(x_distance ** 2 + y_distance ** 2)

    return distance


def validate_path(path: list[int], source: Node, destination: Node) -> None:
    """
    Validates and prints a path from a source node to a destination node.

    Args:
        path (list[int]): The path as a list of node IDs.
        source (Node): The source node.
        destination (Node): The destination node.
    """
    if len(path):
        print(' -> '.join([str(city) for city in path]))
    else:
        print(
            f'There is no path from city {source.id + 1} to {destination.id + 1}')


def initialize_graph(graph: list[Node]) -> None:
    """
    Initializes the graph by setting the initial state of each node.

    Args:
        graph: The graph represented as a list of Node objects.

    """
    for node in graph:
        node.status = Status.NOT_VISITED
        node.estimated_cost = inf
        node.father_node = None


def relax(cur_node: Node, next_node: Node, weight: int) -> None:
    """
    Relaxes an edge between two nodes if a shorter path is found.

    Args:
        cur_node (Node): The current node.
        next_node (Node): The next node connected by the edge.
        weight (int): The weight of the edge.

    """
    if (next_node.estimated_cost > (cur_node.estimated_cost + weight)):
        next_node.estimated_cost = cur_node.estimated_cost + weight
        next_node.father_node = cur_node


def pathway_recursive(node: Node, path: list = []) -> list:
    """
    Recursively finds the path from the given node to its father node.

    Args:
        node: The current node.
        path: The current path. Defaults to an empty list.

    Returns:
        list: The updated path from the given node to its father node.
    """
    if node.father_node == node:
        path.append(node.name)
        return path
    elif node.father_node == None:
        return path
    pathway_recursive(node.father_node, path)
    path.append(node.name)
    return path


if __name__ == '__main__':
    pass
