from random import randint


def random_row(n):
    return [randint(0, 1) for i in range(n)]


def rule90(x, y, z):
    return (x + z) % 2


def next_row(f, row):
    return [f(row[i - 1], row[i], row[i + 1]) for i in range(len(row) - 1)] + [f(row[-2], row[-1], row[0])]


def elementary_ca_rule(n):
    assert 0 <= n <= 255
    return lambda x, y, z: (n >> (4 * x + 2 * y + z)) & 1


def ca_image(f, gen=25, random_init=False):
    assert gen > 0
    if random_init:
        graph = [random_row(2 * gen + 1)]
    else:
        graph = [[0] * gen + [1] + [0] * gen]
    for i in range(gen - 1):
        graph.append(next_row(f, graph[-1]))
    return graph


def find_rule_number(f):
    s = ""
    for i in range(8):
        b1 = (i & 4) >> 2
        b2 = (i & 2) >> 1
        b3 = i & 1
        v = f(b1, b2, b3)
        s = str(v) + s
        print(f"({b1}, {b2}, {b3}) --> {f(b1, b2, b3)}")
    print(f"Rule: binary 0b{s} --> decimal {int(s, 2)}")