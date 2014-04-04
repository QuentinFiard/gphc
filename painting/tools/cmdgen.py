import numpy as np


def paint_block(block):
    """"
    Generates commands for blocks (numpy array)

    Returns
    -------
    string
    """

    block = np.array(block)

    n, m = block.shape

    return "\n".join(["PAINSTSQ %i %i 0" % (R, C) for R in xrange(n)
                      for C in xrange(m) if block[R, C]])


def unpaint_block(block):
    """"
    Generates commands for blocks (numpy array)

    Returns
    -------
    string
    """

    block = np.array(block)

    n, m = block.shape

    return "\n".join(["ERASECELL %i %i" % (R, C) for R in xrange(n)
                      for C in xrange(m) if block[R, C]])


def gencmd(blocks, K=None):
    """
    Generate commands for a set of blocks.

    Returns
    -------
    string

    """

    return "\n".join(map(unpaint_block, blocks))


print gencmd([np.eye(10)])
