import matplotlib.pyplot as plt
import numpy as np


def main():
    a = 0.5
    b = 1.0

    x_array = np.linspace(-8, 8, 101)
    y_array = a * x_array + b

    plt.plot(x_array, y_array)
    plt.axis('equal')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
