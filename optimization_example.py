import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as so

import least_square_left_inverse as li

counter_snapshot = 0


def snapshot(x_array, y_array, y_contaminated_array, y_reconstructed, string_title):
    # not a recommended practice
    global counter_snapshot

    li.snapshot(x_array, y_array, y_contaminated_array, y_reconstructed)
    plt.title('iteration %03d: %s' % (counter_snapshot, string_title))

    snapshot_name = 'snapshot%03d.png' % counter_snapshot
    plt.savefig(snapshot_name, dpi=300)
    counter_snapshot += 1


def cost_function(w, array_y_measurement, mat_x, array_y_signal):
    a_hat, b_hat = w

    mat_w = np.matrix([[a_hat],
                       [b_hat]])

    mat_y_estimation = mat_x * mat_w

    error = array_y_measurement - np.array(mat_y_estimation).flatten()

    cost = sum(error ** 2) / len(array_y_measurement)

    string_title = 'a = %8.3f b = %8.3f' % (a_hat, b_hat)
    snapshot(np.array(mat_x.T[0, :]).flatten(), array_y_signal, array_y_measurement,
             np.array(mat_y_estimation.T).flatten(), string_title)

    return cost


def main():
    x_array, y_array, y_contaminated_array = li.prepare_data_points()

    mat_x = li.x_array_to_mat(x_array)

    initial_guess = np.array((0, 0))
    result = so.minimize(cost_function, initial_guess, args=(y_contaminated_array, mat_x, y_array))
    print('result:\n%s' % result)


if __name__ == '__main__':
    main()
