from to_networkx import to_networkx
import networkx
from networkx.algorithms.community.kernighan_lin import kernighan_lin_bisection


def run(data):
  g = to_networkx(data)
  undirected_g = g.to_undirected()
  a11, a12 = kernighan_lin_bisection(undirected_g, max_iter=1)
  print a11

  # Dummy solution for now.
  return [[data.start] for i in xrange(data.num_cars)]
