from math import sqrt

def main():
    points = [(3, 4), (6, 4), (6, 8)]
    distances = []

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclideanDistance(points[i], points[j])
            distances.append(distance)

    print(min(distances))

def euclideanDistance(point1, point2):
    (x1, y1) = point1
    (x2, y2) = point2
    euclidean_distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return euclidean_distance

main()
