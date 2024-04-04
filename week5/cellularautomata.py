def next_row(f, row):
    return [0] + [f(row[i - 1], row[i], row[i + 1]) for i in range(1, len(row) - 1)] + [0]

def rule(n):
    return lambda x, y, z: (n >> (4 * x + 2 * y + z)) & 1

def ca_image(rule_number, gen=25):
    f = rule(rule_number)
    graph = [[0] * (2 * gen + 1)]
    graph[0][gen] = 1
    for i in range(gen - 1):
        graph.append(next_row(f, graph[-1]))
    return graph

