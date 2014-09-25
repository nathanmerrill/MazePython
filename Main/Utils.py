
def multiply_tuple(tup, scalar):
    return tuple([scalar*x for x in tup])


def add_tuples(tup1, tup2):
    return tuple(map(lambda x, y: x + y, tup1, tup2))


def invert_tuple(tup):
    return tup[::-1]


def multiply_tuples(tup1, tup2):
    return tuple(map(lambda x, y: x * y, tup1, tup2))