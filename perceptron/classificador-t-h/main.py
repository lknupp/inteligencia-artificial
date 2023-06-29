from perceptron import Perceptron


def main():
    ppc: Perceptron = Perceptron(.1, 10)

    while True:
        # l = [1, 0, 0, 1, 0,
        #      0, 1, 0, 0, 1,
        #      0, 0, 1, 1, 1,
        #      0, 0, 1, 0, 1,
        #      0, 0, 1, 0, 1]
        data: list[int] = list(map(int, input('Digite a entrada: ').split()))
        if ppc.predict(data) >= 0:
            print('T')
        else:
            print('H')


def plot_decision_region():
    ...


if __name__ == '__main__':
    main()
