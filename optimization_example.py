import numpy as np
import scipy.optimize as so


def cost_function(w, array_y_measurement, mat_x):
    a_hat, b_hat = w

    mat_w = np.matrix([[a_hat],
                       [b_hat]])

    mat_y_estimation = mat_x * mat_w

    error = array_y_measurement - np.array(mat_y_estimation).flatten()

    cost = sum(error ** 2) / len(array_y_measurement)

    return cost


def main():
    help(so)


if __name__ == '__main__':
    main()
