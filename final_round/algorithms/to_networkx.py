import networkx as nx


def to_networkx(data):
  g = nx.DiGraph()
  for i in xrange(len(data.intersections)):
    g.add_node(
        i, lat=data.intersections[i].lat, long=data.intersections[i].long)
  for road in data.roads:
    g.add_edge(
        road.left, road.right, cost=road.cost, distance=road.distance,
        one_way=road.one_way, weight=road.distance / road.cost)
    if not road.one_way:
      g.add_edge(
          road.right, road.left, cost=road.cost, distance=road.distance,
          one_way=road.one_way, weight=road.distance / road.cost)
  return g
