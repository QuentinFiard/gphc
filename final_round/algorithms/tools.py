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
    return neighbor_dict
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
