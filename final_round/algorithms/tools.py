import structures as struct

def to_dict(roads):
  d = {}
  for road in roads:
    if road.left not in d:
      d[road.left] = {}
    d[road.left][road.right] = road
  return d

def neighbor_roads(intersect_idx, roads):
  if intersect_idx in roads:
    list = []
    neighbor_dict = roads[intersect_idx]
    for key in neighbor_dict:
      list.append(neighbor_dict[key])
    return neighbor_dict
  else:
    return []
