def to_rcs(coords):
  i = coords[0][0]
  j = coords[0][1]
  k = coords[1][0]
  l = coords[0][1]

  s = (k - i - 1)/2
  r = i + s
  c = j + s

  return [r, c, s]
