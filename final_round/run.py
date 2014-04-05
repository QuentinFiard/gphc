import io.input as input
import io.output as output

import algorithms.best_local_path as algo

data = input.file_to_data('data/paris_54000.txt')
vehicle_paths = algo.run(data)
output.output(vehicle_paths)
