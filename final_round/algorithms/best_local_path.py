from tools import *
from copy import deepcopy
import sys
import random

def can_move(remainings):
  for remain in remainings:
    if remain > 0:
      return True
  return False

def best_local_path(intersect_idx, roads, roads_o, remaining, radius=5):
  if radius == 0:
    return [[], 0, 0, 0]
  min_cost = sys.maxint
  max_distance = 0
  best_path = []
  current_malus = 0
  nr = neighbor_roads(intersect_idx, roads)
  if len(nr) < 1:
    current_malus = 1
    nr = neighbor_roads(intersect_idx, roads_o)
  best_malus = current_malus
  for road in nr:
    try:
      roads[road.left].pop(road.right)
    except:
      pass
    try:
      roads[road.right].pop(road.left)
    except:
      pass
    [path, cost, distance, malus] = best_local_path(road.right, roads, roads_o, remaining, radius - 1)
    malus += current_malus
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
    if float(distance - malus * 100) / cost > float(max_distance) / min_cost and remaining > cost:
      best_path = path
      min_cost = cost
      max_distance = distance
      best_malus = current_malus

  try:
    roads[intersect_idx].pop(best_path[0])
  except:
    pass
  try:
    roads[best_path[0]].pop(intersect_idx)
  except:
    pass
  return [best_path, min_cost, max_distance, best_malus]



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
        [path, cost, distance, malus] = best_local_path(paths[car][-1], roads, roads_o, remainings[car])
        remainings[car] -= cost
        paths[car].extend(path)
  return paths
