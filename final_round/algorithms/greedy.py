from tools import *
import copy
import random
from stochastics import sample_neighbor


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
        if random.random() < 0.:
          road = best_neighbor_road(paths[car][-1], roads, remainings[car])
        else:
          # sample next node from ~ multinomial (cost_x / distance_x)_x \in neigh(cur_node)
          road = sample_neighbor(paths[car][-1], roads, remainings[car])

        if not road:
          nr = neighbor_roads(paths[car][-1], orig_roads)
          nr = filter(lambda road: road.cost <= remainings[car], nr)
          # sample from diffusion process on graph
          if nr:
            road = random.choice(nr)
        if not road or road.cost > remainings[car]:
          remainings[car] = 0
          continue
        paths[car].append(road.right)
        remainings[car] -= road.cost
        try:
          del roads[road.left][road.right]
          del roads[road.right][road.left]
        except KeyError:
          pass
  return paths
