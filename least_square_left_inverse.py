import matplotlib.pyplot as plt
import numpy as np
import numpy.random as nr


def main():
    # original parameters
    a = 0.5
    b = 1.0

    # independent varialbe
    x_array = np.linspace(-8, 8, 101)

    # true signal (assumption)
    y_array = a * x_array + b

    # measured signal. contaminated with Gaussian noise
    y_contaminated_array = y_array + nr.normal(size=np.shape(y_array))

    '''apply left inverse'''
    mat_x = np.matrix([x_array,
                       np.ones_like(x_array)]).T

    plt.plot(x_array, y_array, label='ground truth')
    plt.plot(x_array, y_contaminated_array, '.', label='measurement')

    plt.axis('equal')
    plt.grid(True)
    plt.legend(loc=0)
    plt.show()


if __name__ == '__main__':
    main()
