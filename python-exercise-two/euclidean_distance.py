points = [(1, 2), (3, 4), (5, 6), (7, 8)]

def euclidean_distance(point1: int, point2: int):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

distances = [euclidean_distance(points[0], point) for point in points[1:]]

if __name__ == "__main__":
    print(distances)