import structures as st

def file_to_data(filename):
  with open(filename, 'r') as f:
    values = f.readline().split()
    num_intersections = int(values[0])
    num_roads = int(values[1])
    max_time = float(values[2])
    num_cars = int(values[3])
    start = int(values[4])
    intersections = []
    for i in xrange(num_intersections):
      values = f.readline().split()
      intersections.append(st.Intersection(float(values[0], values[1])))
    roads = []
    for i in xrange(num_roads):
      values = f.readline().split()
      roads.append(st.Road(int(
          values[0]), int(values[1]), float(values[3]), float(values[4])))
      if int(values[2]) == 2:
        roads.append(st.Road(int(
            values[1]), int(values[0]), float(values[3]), float(values[4])))
    return st.Data(intersections, roads, max_time, start, num_cars)
