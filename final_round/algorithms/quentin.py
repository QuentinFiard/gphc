from sets import Set
import heapq
import math

from to_networkx import to_networkx
from split_graph import geo_split as split_graph
import networkx
from networkx.algorithms.community.kernighan_lin import kernighan_lin_bisection
from networkx.algorithms.shortest_paths.dense import floyd_warshall
from networkx.algorithms.euler import is_eulerian
from networkx.algorithms.shortest_paths.generic import shortest_path
import structures as st

from algorithms.greedy import run as default_run

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

def compute_closest_to_center_in_subgraph(graph, subgraph):
  nodes = subgraph.nodes(data=True)
  lat_mean = sum(map(lambda x: x[1]["lat"], nodes)) / len(nodes)
  long_mean = sum(map(lambda x: x[1]["long"], nodes)) / len(nodes)
  print nodes[:10]
  return min(nodes, key=lambda x: math.pow(
      lat_mean - x[1]["lat"], 2) + math.pow(long_mean - x[1]["long"], 2))[0]

def compute_time(graph, path):
  res = 0
  for i in xrange(len(path) - 1):
    res += graph[path[i]][path[i + 1]]["cost"]
  return res

def run_cars_in_subgraph(data, graph, start, subgraph, num_cars):
  closest_node = compute_closest_in_subgraph(graph, subgraph, start)
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
      intersections, roads, data.max_time - compute_time(graph, path),
      index_map[closest_node], num_cars)
  default_paths = default_run(new_data)
  res = []
  for path2 in default_paths:
    path2.pop(0)
    for i in xrange(len(path2)):
      path2[i] = inverse_index_map[path2[i]]
    res.append(path + path2)
  return res

def run_cars_near_subgraph(data, graph, start, subgraph, num_cars):
  closest_node = compute_closest_to_center_in_subgraph(graph, subgraph)
  path = shortest_path(graph, start, closest_node)
  new_data = st.Data(
      data.intersections, data.roads, data.max_time - compute_time(graph, path),
      index_map[closest_node], num_cars)
  default_paths = default_run(new_data)
  res = []
  for path2 in default_paths:
    path2.pop(0)
    res.append(path + path2)
  return res

CARS_PER_SUBGRAPH = 2

def run(data):
  g = to_networkx(data)
  subgraphs = split_graph(g, data.num_cars / CARS_PER_SUBGRAPH)
  paths = []
  for subgraph in subgraphs:
    paths.extend(run_cars_in_subgraph(
        data, g, data.start, subgraph, CARS_PER_SUBGRAPH))
  return paths
