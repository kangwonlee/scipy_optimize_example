import os

import least_square_left_inverse as li
import optimization_example as optim


def main():
    import sys

    filename_profile = 'cProfile.result'
    if 2 <= len(sys.argv):
        if 'run' == sys.argv[1]:
            profile(filename_profile)
        elif 'read' == sys.argv[1]:
            if os.path.exists(filename_profile):
                read_profile_result(filename_profile)
            else:
                print('Cannot find result file %s' % filename_profile)
        else:
            print('please choose "read" or "run"')
    else:
        print('please choose "read" or "run"')


def profile(filename_profile):
    import cProfile

    cProfile.run('run_this()', filename_profile)
    read_profile_result(filename_profile)


def read_profile_result(filename_profile):
    import pstats
    p = pstats.Stats(filename_profile)

    p.strip_dirs()
    p.sort_stats('cumulative', 'time')
    p.print_stats(50)


def run_this():
    x_array, y_array, y_contaminated_array = li.prepare_data_points()

    result0 = li.least_square_left_inverse(x_array, y_contaminated_array)
    result1 = optim.optimization_example(x_array, y_contaminated_array)


if __name__ == '__main__':
    main()
