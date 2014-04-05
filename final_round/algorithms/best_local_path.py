from tools import *
from copy import deepcopy
import sys

def can_move(remainings):
  for remain in remainings:
    if remain > 0:
      return True
  return False

def best_local_path(intersect_idx, roads, roads_o, remaining, radius=1):
  if radius == 0:
    return [[], 0, 0]
  min_cost = sys.maxint
  max_distance = 0
  best_path = []
  for road in neighbor_roads(intersect_idx, roads):
    try:
      roads[road.left].pop(road.right)
    except:
      pass
    try:
      roads[road.right].pop(road.left)
    except:
      pass
    [path, cost, distance] = best_local_path(road.right, roads, roads_o, remaining, radius - 1)
    try:
      roads[road.left][road.right] = roads_o[road.left][road.right]
    except:
      pass
    try:
      roads[road.right][road.left] = roads_o[road.right][road.left]
    except:
      pass
    path = [road.right] + path
    cost += road.cost
    distance += road.distance
    if float(distance) / cost > float(max_distance) / min_cost and remaining > cost:
      best_path = path
      min_cost = cost
      max_distance = distance
  return [best_path, min_cost, max_distance]



def run(data):
  roads = to_dict(data.roads)
  roads_o = deepcopy(roads)
  remainings = []
  paths = []
  for car in range(data.num_cars):
    remainings.append(data.max_time)
    paths.append([data.start])

  while can_move(remainings):
    for car in range(data.num_cars):
      if remainings[car] > 0:
        [path, cost, distance] = best_local_path(paths[car][-1], roads, roads_o, remainings[car])
        remainings[car] -= cost
        paths[car].extend(path)
  return paths
