from test import INPUTS, LABELS
from plotter import plot_error_rate
import numpy as np


class Perceptron:
    __slots__ = ('__eta', '__epochs', '__weights', '__errors')

    def __init__(self, eta: float = 0.2, epochs: int = 10) -> None:
        self.__eta: float = eta
        self.__epochs: int = epochs
        self.__weights: list = None
        self.__errors: list[float] = list()
        self.fit(INPUTS, LABELS)

    def fit(self, inputs: list[int], labels: list[int]) -> None:
        self.__weights = np.zeros(1 + np.shape(inputs)[1])

        for _ in range(self.__epochs):
            error: int = 0
            for input, target in zip(inputs, labels):
                update: float = self.__eta * (target - self.predict(input))
                self.__weights[1:] += update * np.array(input)
                self.__weights[0] += update
                error += int(update != 0.0)
            self.__errors.append(error)
        plot_error_rate(self.__errors)

    def predict(self, inputs: list[float]) -> float:
        return np.where(self.net_input(inputs) >= 0, 1, -1)

    def net_input(self, input) -> float:
        return np.dot(np.array(input), self.__weights[1:]) + self.__weights[0]

    def activation_function(self, number: float) -> float:
        return 1 / (1 + np.exp(-number))
