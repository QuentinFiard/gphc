import tools.parser as ps
import tools.commands as cmd

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

print cmd.count(block, erased)
print cmd.paint_all(block).rstrip('\n')
