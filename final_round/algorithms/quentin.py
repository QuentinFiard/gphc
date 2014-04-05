from sets import Set
import heapq

from to_networkx import to_networkx
from split_graph import geo_split as split_graph
import networkx
from networkx.algorithms.community.kernighan_lin import kernighan_lin_bisection
from networkx.algorithms.shortest_paths.dense import floyd_warshall
from networkx.algorithms.euler import is_eulerian
from networkx.algorithms.shortest_paths.generic import shortest_path


def compute_closest_in_subgraph(graph, subgraph, start, key="cost"):
  visited = Set()
  heap = [(0, start)]
  while True:
    cost, node = heapq.heappop(heap)
    if subgraph.has_node(node):
      return node
    visited.add(node)
    for neighbor, data in graph[node].iteritems():
      if neighbor not in visited:
        heapq.heappush(
            heap, (cost + data[key], neighbor))

def run_car_in_subgraph(graph, start, subgraph):
  closest_node = compute_closest_in_subgraph(graph, subgraph, start)
  path = shortest_path(graph, start, closest_node)
  print path
  return [start]




def run(data):
  g = to_networkx(data)
  subgraphs = split_graph(g, data.num_cars)
  paths = []
  for subgraph in subgraphs:
    paths.append(run_car_in_subgraph(g, data.start, subgraph))

  return paths
