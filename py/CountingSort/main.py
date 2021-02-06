def get_min_and_max(array):
    return [
        min(array),
        max(array)
    ]

def get_mapping(minimum, maximum):
    mapping = []

    for i in range(minimum, maximum + 1):
        mapping.append([i, 0])

    return mapping

def sort(array):
    minimum, maximum = get_min_and_max(array)
    mapping = get_mapping(minimum, maximum)
    result = []

    for elem in array:
        mapping[elem - minimum][1] += 1

    for pair in mapping:
        for i in range(pair[1]):
            result.append(pair[0])

    return result

print(sort([6, 2, 4, 3, 1, 3]))