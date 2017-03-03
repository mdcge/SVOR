from random import shuffle
from math import sqrt
import numpy as np

coordinates = []

with open('coordinates.txt') as data:
    for line in data:
        _, x, y = map(int, line.split())
        coordinates.append((x,y))

def total_wait_time(order, pos=coordinates):
    distances = [ distance(pos[a], pos[b])
                  for a,b in zip(order[1:], order[:-1]) ]
    wait_times = np.cumsum(distances)
    return round(wait_times.sum())

def distance(a,b):
    xa, ya = a
    xb, yb = b
    dx = xa - xb
    dy = ya - yb
    return sqrt(dx*dx + dy*dy)

def random_search():
    best = 212152
    order = list(range(1,30))
    while True:
        shuffle(order)
        full_order = [0] + order
        new = total_wait_time(full_order)
        if new < best:
            best = new
            best_order = full_order
            print(best, best_order)
