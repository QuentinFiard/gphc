import sys

import io.input as input
import io.output as output
import algorithms.greedy as algo
from autorun import get_score


data = input.file_to_data('data/paris_54000.txt')
vehicle_paths = algo.run(data)
sys.stderr.write("%f\n" % get_score(data, vehicle_paths))
output.output(vehicle_paths)
# print "#" * 100
# score = 0
# for p in vehicle_paths:
#     for j in xrange(len(p) - 1):
#         for road in data.roats:
#             if road.left, road.right == (p[j], p[j + 1])
# print data.roads[0]
