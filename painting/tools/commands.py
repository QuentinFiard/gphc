def to_rcs(coords):
  i = coords[0][0]
  j = coords[0][1]
  k = coords[1][0]
  l = coords[0][1]

  s = (k - i - 1)/2
  if s < 0:
    s = 0
  r = i + s
  c = j + s

  return [r, c, s]

def count(block, erase):
  return str(len(block) + len(erase))

def do_block(block):
    """
    block is a triplet (R, C, S).

    Returns string

    """

    R, C, S = to_rcs(block)

    return 'PAINTSQ %i %i %i' % (R, C, S)


def erase(cell):
    return "ERASECELL %i %i" % cell


def erase_all(cells):
    return "\n".join(map(erase, cells))


def paint_all(blocks):
    return "\n".join(map(do_block, blocks))
