def output(vehicle_paths, show=False):
    solution = []
    num_vehicles = len(vehicle_paths)
    solution.append(str(num_vehicles))

    for path in vehicle_paths:
        solution.append(str(len(path)))
        solution += map(str, path)

    print('\n'.join(solution))


if __name__ == '__main__':
    output([[1,2,3], [4,5,6]])
