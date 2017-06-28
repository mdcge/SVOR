from math import sqrt
from operator import itemgetter
from random import shuffle, randrange
from multiprocessing import Pool
import numpy as np
import matplotlib.pyplot as plt

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
    from time import time
    start = time()
    best = 212152
    order = list(range(1,30))
    for _ in range(N):
        shuffle(order)
        full_order = [0] + order
        new, new_order = hill_climb(full_order)
        if new < best:
            best = new
            best_order = new_order
            #print(best, best_order)
        if best < 70407:
            return (time() - start)
    return best, best_order

while True:
    print(random_search(100000))

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
                # Swap i and j
                swap_order = order[:]
                swap_order[i], swap_order[j] = swap_order[j], swap_order[i]
                swap_cost = total_wait_time(swap_order)
                # Reverse between i and j inclusive
                rev_order = order[:]
                rev_order[i:j+1] = rev_order[j:i-1:-1]
                rev_cost = total_wait_time(rev_order)
                if rev_cost < swap_cost:
                    cost = rev_cost
                    new_order = rev_order
                else:
                    cost = swap_cost
                    new_order = swap_order
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


def show_path(order, coordinates):
    x, y = np.array(coordinates)[order].T
    print(x,y)
    plt.plot(x, y, marker='o')
    plt.show()
