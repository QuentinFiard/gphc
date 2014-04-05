import io.input as input
import io.output as output
import sys
import algorithms.greedy as algo


def get_score(data, vehicle_paths):
    N = len(vehicle_paths)
    score = 0
    visited = {}
    for v_path in vehicle_paths:
        for i in v_path:
            road = data.roads[i]
            if road in visited:
                continue
            visited[road] = True
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


