def file_to_matrix(filename):
  matrix_buffer = []
  with open(filename, 'r') as f:
    f.readline()
    for line in f:
      line_buffer = []
      for char in line:
        if char == '.':
          line_buffer.append(False)
        elif char == '#':
          line_buffer.append(True)
      matrix_buffer.append(line_buffer)
    f.close
  return matrix_buffer

print file_to_matrix('../data/simple.txt')
