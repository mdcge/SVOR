coordinates = []

with open('coordinates.txt') as data:
    for line in data:
        _, x, y = map(int, line.split())
        coordinates.append((x,y))

