def file_to_problem(filename):
  with open(filename, 'r') as f:
    return f.readline()
