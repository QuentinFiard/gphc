from cmdgen import to_rcs


def do_block(block):
    """
    block is a triplet (R, C, S).

    Returns string

    """

    R, C, S = to_rcs(block)

    return 'PAINSTSQ %i %i %i' % (R, C, S)


def erase(cell):
    return "ERASECELL %i %i" % cell


def erase_all(cells):
    return "\n".join(map(erase, cells))


def paint_all(blocks):
    return "\n".join(map(do_block, blocks))

print paint_all([[[0, 10], [101, 100]], [[0, 10], [100, 103]]])
print erase_all([(4, 3), (0, 1)])
