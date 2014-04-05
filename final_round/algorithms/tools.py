import structures as struct

def to_dict(roads):
  d = {}
  for road in roads:
    if road.left not in d:
      d[road.left] = {}
    d[road.left][road.right] = road
  return d

def neighbor_roads(intersect_idx, roads_dict):
  if intersect_idx in roads_dict:
    list = []
    neighbor_dict = roads_dict[intersect_idx]
    for key in neighbor_dict:
      list.append(neighbor_dict[key])
    return list
  else:
    return []

def opposite_road(road, roads_dict):
  if road.right in roads_dict:
    if road.left in roads_dict[road.right]:
      return roads_dict[road.right][road.left]
  return None

def least_expensive_road(intersect_idx, roads_dict):
  n = neighbor_roads(intersect_idx, roads_dict)
  if len(n) > 0:
    minimal = n[0]
    for road in n:
      if road.cost < minimal.cost:
        minimal = road
    return minimal
  return None


def best_neighbor_road(intersect_idx, roads_dict):
  n = neighbor_roads(intersect_idx, roads_dict)
  if len(n) > 0:
    ratio = n[0].distance / n[0].cost
    minimal = n[0]
    for road in n:
      local_ratio = road.distance / road.cost
      if local_ratio < ratio:
        minimal = road
        ratio = local_ratio
    return minimal
  return None

  # n = neighbor_roads(intersect_idx, roads_dict)
  # p = get_paths_from(intersect_idx, roads_dict, radius = 1)
  # best = 1e10
  # key = None
  # i = None
  # for j, s in enumerate(p):
  #   if s[1] < best:
  #     best = s[1]
  #     i = j
  # if i:
  #   print p[i]
  # scores = map(path_ratio, [[x] for x in n])
  # if len(scores) == 0: return None
  # best = 1e10
  # i = None
  # for j, s in enumerate(scores):
  #   if s < best:
  #     best = s
  #     i = j
  # return n[i]
  
  # if len(n) > 0:
  #   ratio = n[0].distance / n[0].cost
  #   minimal = n[0]
  #   for road in n:
  #     local_ratio = road.distance / road.cost
  #     if local_ratio < ratio:
  #       minimal = road
  #       ratio = local_ratio
  #   return minimal
  # return None


def path_ratio(path):
  '''
  Get path ratio.

  '''

  s = 0
  for n in path:
    s += 1. * n.distance / n.cost

  return s


def get_paths_from(i, roads_dict, radius=1):
  neighbors = neighbor_roads(i, roads_dict)
  if radius == 1:
    return [([n], path_ratio([n])) for n in neighbors]

  return [[n] + get_paths_from(n.right, roads_dict, radius=radius - 1)
          for n in neighbors]


def best_neighbor_path(intersect_idx, roads_dict, radius=1):
  n = neighbor_roads(intersect_idx, roads_dict)
  if len(n) > 0:
    ratio = n[0].distance / n[0].cost
    minimal = n[0]
    for road in n:
      local_ratio = road.distance / road.cost
      if local_ratio < ratio:
        minimal = road
        ratio = local_ratio
    # return ratio, minimal

  net_ratio = ratio
  paths = [minimal]

  if radius < 2:
    return net_ratio, paths

  
    return None
