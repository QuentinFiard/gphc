class Intersection(object):
  """An intersection"""
  def __init__(self, lat, long):
    self.lat = lat
    self.long = long


class Road(object):
  """A road"""
  def __init__(self, left, right, cost, distance, one_way):
    self.left = left
    self.right = right
    self.cost = cost
    self.distance = distance
    self.one_way = one_way


class Data(object):
  """Problem data"""
  def __init__(self, intersections, roads, max_time, start, num_cars):
    self.intersections = intersections
    self.roads = roads
    self.max_time = max_time
    self.start = start
    self.num_cars = num_cars
