import io.input as input
import io.output as output

import algorithms.trivial as trivial

problem = input.file_to_problem('data/task.txt')

solution = trivial.run(problem)

output.show(solution)
