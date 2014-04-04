

def do_block(block):
    """
    block is a triplet (R, C, S).

    Returns string

    """

    R, C, S = block

    return 'PAINSTSQ %i %i %i' % (R, C, S)


def paint_all(blocks):
    return "\n".join(map(do_block, blocks))

print paint_all([(1, 0, 5), (3, 4, 10)])
