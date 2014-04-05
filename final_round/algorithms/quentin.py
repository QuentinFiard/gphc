from sets import Set
import heapq

from to_networkx import to_networkx
from split_graph import geo_split as split_graph
import networkx
from networkx.algorithms.community.kernighan_lin import kernighan_lin_bisection
from networkx.algorithms.shortest_paths.dense import floyd_warshall
from networkx.algorithms.euler import is_eulerian
from networkx.algorithms.shortest_paths.generic import shortest_path
import structures as st

from algorithms.greedy import run as greedy_run

def compute_closest_in_subgraph(graph, subgraph, start, key="cost"):
  visited = Set()
  heap = [(0, start)]
  while True:
    cost, node = heapq.heappop(heap)
    if subgraph.has_node(node):
      return node, cost
    visited.add(node)
    for neighbor, data in graph[node].iteritems():
      if neighbor not in visited:
        heapq.heappush(
            heap, (cost + data[key], neighbor))


def run_car_in_subgraph(data, graph, start, subgraph):
  # print data.max_time
  closest_node, cost = compute_closest_in_subgraph(graph, subgraph, start)
  # print cost
  path = shortest_path(graph, start, closest_node)
  nodes = subgraph.nodes(data=True)
  intersections = map(
      lambda node: st.Intersection(node[1]["lat"], node[1]["long"]),
      nodes)
  index_map = {}
  inverse_index_map = {}
  for i in xrange(len(nodes)):
    index_map[nodes[i][0]] = i
    inverse_index_map[i] = nodes[i][0]
  roads = map(
      lambda edge: st.Road(
          index_map[edge[0]], index_map[edge[1]], edge[2]["cost"],
          edge[2]["distance"], edge[2]["one_way"]),
      subgraph.edges(data=True))
  new_data = st.Data(
      intersections, roads, data.max_time - cost, index_map[closest_node], 1)
  path2 = greedy_run(new_data)[0]
  path2.pop(0)
  for i in xrange(len(path2)):
    path2[i] = inverse_index_map[path2[i]]
  # print "%d -> %d" % (path[-1], path2[0])
  return path + path2




def run(data):
  g = to_networkx(data)
  subgraphs = split_graph(g, data.num_cars)
  paths = []
  for subgraph in subgraphs:
    paths.append(run_car_in_subgraph(data, g, data.start, subgraph))

  return paths
