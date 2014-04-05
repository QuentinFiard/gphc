import sys
from subprocess import Popen, PIPE

if __name__ == '__main__':
  assert len(sys.argv) == 3
  num_runs = int(sys.argv[1])
  max_score = None
  for i in xrange(num_runs):
    stdout, stderr = Popen(
        ["/usr/bin/env", "python", "run.py"], stdout=PIPE,
        stderr=PIPE).communicate()
    score = float(stderr)
    if not max_score or max_score < score:
      max_score = score
      print score
      with open(sys.argv[2], "w") as f:
        f.write(stdout)
