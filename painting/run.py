import tools.parser as ps
import tools.commands as cmd
<<<<<<< Updated upstream
<<<<<<< Updated upstream
import tools.bruteforce as btf
import sys
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes

def dumb(matrix):
  block = []
  i = 0
  j = 0
  for line in matrix:
    for char in line:
      if char:
        block.append([[i, j], [i, j]])
      j += 1
    i += 1
    j = 0
  return [block, []]

GRID_SIZE = 6

def translate_cmds(cmds, x, y):
  blocks = []
  to_erase = []
  for block in cmds[0]:
    blocks.append(((block[0][0] + x, block[0][1] + y), (block[1][0] + x, block[1][1] + y)))
  for erased in cmds[1]:
    to_erase.append((erased[0] + x, erased[1] + y))
  return [blocks, to_erase]

def optimized(matrix):
  res = [[], []]
  num_blocks = (len(matrix) / GRID_SIZE) * (len(matrix[0]) / GRID_SIZE)
  num_processed = 0
  for i in xrange(len(matrix) / GRID_SIZE):
    for j in xrange(len(matrix[0]) / GRID_SIZE):
      image = []
      for x in xrange(min(GRID_SIZE, len(matrix) - GRID_SIZE * i)):
        row = []
        for y in xrange(min(GRID_SIZE, len(matrix[0]) - GRID_SIZE * j)):
          row.append(matrix[GRID_SIZE * i + x][GRID_SIZE * j + y])
        image.append(tuple(row))
      image = tuple(image)
      cmds = translate_cmds(btf.BruteForce(image), GRID_SIZE * i, GRID_SIZE * j)
      res[0] += cmds[0]
      res[1] += cmds[1]
      num_processed += 1
      sys.stderr.write("processed %d / %d\n" % (num_processed, num_blocks))
  return res

matrix = ps.file_to_matrix('data/doodle.txt')

<<<<<<< Updated upstream
[block, erased] = optimized(matrix)

print cmd.count(block, erased)
print cmd.paint_all(block).rstrip('\n')
print cmd.erase_all(erased)
=======
[block, erased] = dumb(matrix)

print cmd.paint_all(block)
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
