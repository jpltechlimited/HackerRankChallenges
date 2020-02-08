def print_formatted(number):
    padding = len(bin(number)[2:])
    for i in range(1, n + 1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w=padding))


if __name__ == '__main__':
    n = 2
    print_formatted(n)
