import pylab


def main():
    x = pylab.linspace(-3, 3, 101)
    y = x ** 2 + 1

    xd = pylab.arange(-3, 3+0.1, 0.2)
    yd = xd ** 2 + 1

    pylab.plot(x, y)
    pylab.plot(xd, yd, '.')
    pylab.grid(True)
    pylab.xlim([-3, 3])
    pylab.ylim([0, 6])

    pylab.savefig('plot_x2_1.png', dpi=300)

if __name__ == '__main__':

    main()
