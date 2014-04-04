def file_to_matrix(filename):
  f = open(filename, 'w')
  f.readline() # Skip header
  matrix_buffer = []
  line_index = 0
  char_index = 0
  first_pass = True
  with open(filename, 'w') as f:
    if first_pass:
      f.readline()
      first_pass = False
    elif char == '\n':
      line_index += 1
      char_index = 0
      matrix_buffer[line_index] = []
    elif char == '.':
      matrix_buffer[line_index][char_index] = False
      char_index += 1
    elif char == '#':
      matrix_buffer[line_index][char_index] = True
      char_index += 1
  return matrix_buffer
