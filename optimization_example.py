import numpy as np
import scipy.optimize as so

import least_square_left_inverse as li


def cost_function(w, array_y_measurement, mat_x):
    a_hat, b_hat = w

    mat_w = np.matrix([[a_hat],
                       [b_hat]])

    mat_y_estimation = mat_x * mat_w

    error = array_y_measurement - np.array(mat_y_estimation).flatten()

    cost = sum(error ** 2) / len(array_y_measurement)

    return cost


def main():
    x_array, y_array, y_contaminated_array = li.prepare_data_points()

    mat_x = li.x_array_to_mat(x_array)

    initial_guess = np.array((0, 0))
    result = so.minimize(cost_function, initial_guess, args=(y_contaminated_array, mat_x))
    print('result:\n%s' % result)


if __name__ == '__main__':
    main()
