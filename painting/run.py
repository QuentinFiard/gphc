import tools.parser as ps

def dumb(matrix):
  block = []
  i = 0
  j = 0
  for line in matrix:
    i += 1
    for char in line:
      j += 1
      if char:
        block.append([[i, j], [i, j]])
    j = 0
  return [block, []]


matrix = ps.file_to_matrix('data/doodle.txt')

[block, erased] = dumb(matrix)
