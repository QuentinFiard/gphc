import io.input as input
import algorithms.trivial as algo

data = input.file_to_data('data/paris_54000.txt')

has_exit = [False for i in xrange(len(data.intersections))]

for edge in data.roads:
  has_exit[edge.left] = True
  if not edge.one_way:
    has_exit[edge.right] = True

for i in xrange(len(has_exit)):
  if not has_exit[i]:
    print "Intersection %d has no exit" % i
