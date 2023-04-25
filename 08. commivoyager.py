import math

def tsp_brute_force(points):
    n = len(points)
    if n == 0:
        return [], 0
    elif n == 1:
        return [points[0]], 0

    shortest_path = None
    shortest_distance = float('inf')

    for i in range(n):
        # Choose a starting point for the path
        start = points[i]

        # Generate all possible paths starting from the chosen starting point
        paths = [[start] + list(perm) for perm in generate_permutations(points[:i] + points[i+1:])]

        # Calculate the distance of each path and keep track of the shortest path
        for path in paths:
            distance = calculate_distance(path)
            if distance < shortest_distance:
                shortest_distance = distance
                shortest_path = path

    return shortest_path, shortest_distance

def generate_permutations(points):
    n = len(points)
    if n == 0:
        yield []
    elif n == 1:
        yield points

    for i in range(n):
        for perm in generate_permutations(points[:i] + points[i+1:]):
            yield [points[i]] + perm

def calculate_distance(path):
    distance = 0
    for i in range(len(path) - 1):
        distance += math.sqrt((path[i][0] - path[i+1][0])**2 + (path[i][1] - path[i+1][1])**2)
    distance += math.sqrt((path[-1][0] - path[0][0])**2 + (path[-1][1] - path[0][1])**2)
    return distance

points = [(0, 0), (1, 1), (2, 2), (3, 3)]
shortest_path, shortest_distance = tsp_brute_force(points)
print(shortest_path)
print(shortest_distance)