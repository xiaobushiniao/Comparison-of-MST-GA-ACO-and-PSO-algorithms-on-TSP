# -*- coding: utf-8 -*-
import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import random
import numpy as np
from utils.distance import calc_distance_matrix

def pso_tsp(dist_matrix, n, num_particles=30, iterations=100, w=0.8, c1=1.5, c2=1.5):
    def random_permutation():
        perm = list(range(1, n))
        random.shuffle(perm)
        return [0] + perm + [0]

    def get_length(path):
        return sum(dist_matrix[path[i]][path[i+1]] for i in range(len(path)-1))

    particles = [random_permutation() for _ in range(num_particles)]
    pbest = particles.copy()
    pbest_len = [get_length(p) for p in particles]
    gbest = min(particles, key=get_length)
    gbest_len = get_length(gbest)

    for _ in range(iterations):
        for i in range(num_particles):
            new_path = particles[i].copy()
            for _ in range(int(w * n)):
                a, b = random.sample(range(1, n), 2)
                new_path[a], new_path[b] = new_path[b], new_path[a]
            if random.random() < c1:
                a, b = random.sample(range(1, n), 2)
                new_path[a], new_path[b] = pbest[i][a], pbest[i][b]
            if random.random() < c2:
                a, b = random.sample(range(1, n), 2)
                new_path[a], new_path[b] = gbest[a], gbest[b]
            new_len = get_length(new_path)
            if new_len < pbest_len[i]:
                pbest[i], pbest_len[i] = new_path, new_len
                if new_len < gbest_len:
                    gbest, gbest_len = new_path, new_len
            particles[i] = new_path
    return gbest, gbest_len

if __name__ == "__main__":
    coords = np.load("data/coords.npy")
    dist_matrix = calc_distance_matrix(coords)
    n = len(coords)
    path, length = pso_tsp(dist_matrix, n)
    print("微粒群算法路径:", path)
    print("路径长度:", round(length, 2))