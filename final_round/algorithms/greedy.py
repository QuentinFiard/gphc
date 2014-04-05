from tools import *
import copy
import random

def can_move(remainings):
  for remain in remainings:
    if remain > 0:
      return True
  return False

def run(data):
  roads = to_dict(data.roads)
  # orig_roads = copy.deepcopy(roads)
  orig_roads = to_dict(data.roads)
  remainings = []
  paths = []
  for car in range(data.num_cars):
    remainings.append(data.max_time)
    paths.append([data.start])

  while can_move(remainings):
    for car in range(data.num_cars):
      if remainings[car] > 0:
        road = best_neighbor_road(paths[car][-1], roads)
        if road:
          if road.cost > remainings[car]:
            road = None
        if not road:
          road = least_expensive_road(paths[car][-1], roads)
        if not road:
          nr =  neighbor_roads(paths[car][-1], orig_roads)

          # sample from diffusion process on graph
          if nr:
            # road = random.choice(nr)
            for _ in xrange(10):
              random.shuffle(nr)
            road = nr[0]

          # road = best_neighbor_road(paths[car][-1], orig_roads)
        if not road or road.cost > remainings[car]:
          road = None
        if road: # open
          paths[car].append(road.right)
          remainings[car] -= road.cost
          try:
            roads[road.left].pop(road.right)
            roads[road.right].pop(road.left)
          except KeyError:
            pass
        else:
          remainings[car] = 0
  return paths