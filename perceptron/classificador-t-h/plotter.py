import matplotlib.pyplot as plt
import os


def plot_error_rate(errors: list[float], classifier: str = ''):
    plt.plot(range(1, len(errors) + 1), errors, marker='o')
    plt.xlabel('Epochs')
    plt.ylabel('Number of missclassifications')
    # plt.show()
    fig = plt.gcf()
    file_path: str = os.path.join(os.path.dirname(__file__), 'assets')
    try:
        os.mkdir(file_path)
    except FileExistsError:
        pass
    file_name: str = None
    if classifier:
        file_name = ''.join(classifier, '-error-rate.png')
    else:
        file_name = ''.join('error-rate.png')
    fig.savefig(os.path.join(file_path, file_name), dpi=300)
