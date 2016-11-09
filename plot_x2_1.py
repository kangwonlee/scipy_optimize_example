import pylab


def main():
    x = pylab.linspace(-2, 2, 101)
    y = x ** 2 + 1
    pylab.plot(x, y)
    pylab.grid(True)

    pylab.savefig('plot_x2_1.png', dpi=300)

if __name__ == '__main__':

    main()
