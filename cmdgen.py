import numpy as np


def do_block(block):
    n, m = block.shape

    return "\n".join(["PAINSTSQ %i %i 0" % (R, C) for R in xrange(n)
                      for C in xrange(m) if block[R, C]])


def gencmd(blocks, K=None):
    return "\n".join(map(do_block, blocks))


print gencmd([np.eye(10)])
