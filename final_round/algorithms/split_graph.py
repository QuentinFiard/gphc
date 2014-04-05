import math
from sets import Set

def check_power_of_2(n):
  l = math.log(n, 2)
  if math.floor(l) != l:
    print "%d is not a power of 2" % n
    assert False

def simple_split(g, n):
  check_power_of_2(n)
  if n == 1:
    return g
  if n > 2:
    [a, b] = simple_split(g, 2)
    return simple_split(a, n / 2) + simple_split(b, n / 2)

def geo_split(g, n):
  check_power_of_2(n)
  if n == 1:
    return g
  if n > 2:
    [a, b] = geo_split(g, 2)
    return geo_split(a, n / 2) + geo_split(b, n / 2)
  nodes = g.nodes(data=True)
  if (max(nodes, key=lambda pair: pair[1]["lat"])[1]["lat"] -
      min(nodes, key=lambda pair: pair[1]["lat"])[1]["lat"] >
      max(nodes, key=lambda pair: pair[1]["long"])[1]["long"] -
      min(nodes, key=lambda pair: pair[1]["long"])[1]["long"]):
    key = "lat"
  else:
    key = "long"
  nodes.sort(key=lambda pair: pair[1][key])
  nodes = map(lambda pair: pair[0], nodes)
  a = g.subgraph(nodes[:len(nodes)/2])
  b = g.subgraph(nodes[len(nodes)/2:])
  return [a, b]
