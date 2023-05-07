from dataclasses import dataclass


class Coordinate:
    def __init__(self, x_coordinate: int, y_coordinate: int) -> None:
        self.x_coordinate: int = x_coordinate
        self.y_coordinate: int = y_coordinate
