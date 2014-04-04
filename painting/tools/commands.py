from cmdgen import to_rcs


def do_block(block):
    """
    block is a triplet (R, C, S).

    Returns string

    """

    R, C, S = to_rcs(block)

    return 'PAINSTSQ %i %i %i' % (R, C, S)


def paint_all(blocks):
    return "\n".join(map(do_block, blocks))

print paint_all([[[0, 10], [101, 100]], [[0, 10], [100, 103]]])
