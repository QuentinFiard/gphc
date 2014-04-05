def output(vehicle_paths, path_name=None):
    solution = []
    num_vehicles = len(vehicle_paths)
    solution.append(str(num_vehicles))

    for path in vehicle_paths:
        solution.append(str(len(path)))
        solution += map(str, path)

    if path_name is None:
        print('\n'.join(solution))
    else:
        with open(path_name, 'w') as f:
            f.write('\n'.join(solution))


if __name__ == '__main__':
    output([[1,2,3], [4,5,6]])
