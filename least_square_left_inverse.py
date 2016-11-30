import matplotlib.pyplot as plt
import numpy as np
import numpy.random as nr


def main():
    # original parameters
    a = 0.5
    b = 1.0

    x_array, y_array, y_contaminated_array = prepare_data_points(a=a, b=b)

    estimation, y_reconstructed = least_square_left_inverse(x_array, y_contaminated_array)
    print('estimation of a = %g' % estimation[0, 0])
    print('estimation of b = %g' % estimation[1, 0])

    snapshot(x_array, y_array, y_contaminated_array, y_reconstructed)
    plt.show()


def snapshot(array_x, array_y_signal, array_y_contaminated, array_y_reconstructed):
    '''visualize'''
    plt.clf()
    plt.plot(array_x, array_y_reconstructed, label='reconstructed')
    plt.plot(array_x, array_y_contaminated, '.', label='measurement')
    plt.plot(array_x, array_y_signal, label='ground truth')
    axis_grid_legend()


def axis_grid_legend():
    plt.axis('equal')
    plt.grid(True)
    plt.legend(loc=0)


def least_square_left_inverse(x_array, y_contaminated_array):
    '''prepare left inverse'''
    mat_x = x_array_to_mat(x_array)
    mat_xt = mat_x.T
    mat_xt_x = mat_xt * mat_x
    mat_left_inv = mat_xt_x.I * mat_xt
    '''multiply left inverse with the measurement'''
    y_contaminated_matrix = np.matrix([y_contaminated_array]).T
    '''reconstruct the signal'''
    estimation = mat_left_inv * y_contaminated_matrix
    y_reconstructed = mat_x * estimation
    return estimation, y_reconstructed


def x_array_to_mat(x_array):
    mat_x = np.matrix([x_array,
                       np.ones_like(x_array)]).T
    return mat_x


def prepare_data_points(n_interval=100, a=0.5, b=1.0):
    n_points = n_interval + 1
    # independent varialbe
    x_array = np.linspace(-8, 8, n_points)
    # true signal (assumption)
    y_array = a * x_array + b
    # measured signal. contaminated with Gaussian noise
    y_contaminated_array = y_array + nr.normal(size=np.shape(y_array))
    return x_array, y_array, y_contaminated_array


if __name__ == '__main__':
    main()
