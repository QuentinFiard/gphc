def to_rcs(coords):
  i = coords[0][0]
  j = coords[0][1]
  k = coords[1][0]
  l = coords[0][1]

  s = (k - i - 1)/2
  r = i + s
  c = j + s

# <<<<<<< HEAD
# def paint(block):
#     R, C, S = block
#     return "PAINSTSQ %i %i 0
# def paint_block(block):
#     """"
#     Generates commands for blocks (numpy array)

#     Returns
#     -------
#     string
#     """

#     block = np.array(block)

#     n, m = block.shape

#     return "\n".join(["PAINSTSQ %i %i 0" % (R, C) for R in xrange(n)
#                       for C in xrange(m) if block[R, C]])


# def unpaint_block(block):
#     """"
#     Generates commands for blocks (numpy array)

#     Returns
#     -------
#     string
#     """

#     block = np.array(block)

#     n, m = block.shape

#     return "\n".join(["ERASECELL %i %i" % (R, C) for R in xrange(n)
#                       for C in xrange(m) if block[R, C]])


# def gencmd(blocks, K=None):
#     """
#     Generate commands for a set of blocks.

#     Returns
#     -------
#     string

#     """

#     return "\n".join(map(unpaint_block, blocks))


# print gencmd([np.eye(10)])
# d = open(sys.arg[1]
# from parser import file_to_matrix

# print file_to_matrix(
# =======
  return [r, c, s]
# >>>>>>> 07a03322ccae4c51e3b7e2e8622d1b4b78e99b7f
