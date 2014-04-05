import math

def get_num_split(n):
  l = math.log(n, 2)
  if math.floor(l) != l:
    print "%d is not a power of 2" % n
    assert False
  return l

def simple_split(g, n):
  num_split = get_num_split(n)
  pass
