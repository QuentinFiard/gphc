import io.input as input
import io.output as output
import sys
import algorithms.greedy as algo
from algorithms.tools import to_dict


def get_score(data, vehicle_paths):
    roads = to_dict(data.roads)
    score = 0
    visited = set()
    for path in vehicle_paths:
        for i in xrange(len(path) - 1):
            road = roads[path[i]][path[i + 1]]
            edge = (min(road.left, road.right), max(road.left, road.right))
            if edge in visited:
                continue
            visited.add(edge)
            score += road.distance
    return score

if __name__ == '__main__':
    data = input.file_to_data('data/paris_54000.txt')
    N = int(sys.argv[1])
    best_score = 0

    for i in range(N):
        vehicle_paths = algo.run(data)
        score = get_score(data, vehicle_paths)
        if score > best_score:
            best_score = score
            best_result = vehicle_paths

    path_name = "answers/answer.txt"
    print best_score
    output.output(vehicle_paths, path_name)


