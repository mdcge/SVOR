from math import sqrt
from operator import itemgetter
from random import shuffle, randrange
from multiprocessing import Pool
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

def random_search(N):
    best = 212152
    order = list(range(1,30))
    for _ in range(N):
        shuffle(order)
        full_order = [0] + order
        new, new_order = hill_climb(full_order)
        if new < best:
            best = new
            best_order = new_order
    return best, best_order

def parallel_random_search():
    best = 212152
    with Pool(8) as p:
        jobs = [10] * 8
        while True:
            new, new_order = min(p.map(random_search, jobs), key = itemgetter(0))
            if new < best:
                best = new
                best_order = new_order
                print(best, best_order)

def hill_climb(order):
    best = 2121520
    L = len(order)
    improved = True
    while improved:
        improved = False
        for i in range(1, L):
            for j in range(i+1, L):
                new_order = order[:]
                new_order[i], new_order[j] = new_order[j], new_order[i]
                cost = total_wait_time(new_order)
                if cost < best:
                    improved = True
                    best = cost
                    best_order = new_order[:]
        order = best_order
    return best, best_order

def swap_random_pair(order):
    L = len(order)
    a,b = randrange(1,L), randrange(1,L)
    order[a], order[b] = order[b], order[a]
