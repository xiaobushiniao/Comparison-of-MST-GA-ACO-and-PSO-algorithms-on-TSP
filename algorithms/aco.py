# -*- coding: utf-8 -*-
import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from utils.distance import calc_distance_matrix

def aco_tsp(dist_matrix, n, num_ants=20, num_iterations=100, alpha=1.0, beta=5.0, rho=0.1, q=1.0):
    pheromone = np.ones_like(dist_matrix)
    best_length = float('inf')
    best_path = None
    for _ in range(num_iterations):
        all_paths = []
        for _ in range(num_ants):
            path = [0]
            visited = set(path)
            for _ in range(n-1):
                i = path[-1]
                probs = []
                for j in range(n):
                    if j not in visited:
                        probs.append((pheromone[i][j] ** alpha) * ((1.0 / dist_matrix[i][j]) ** beta))
                    else:
                        probs.append(0)
                probs = probs / np.sum(probs)
                j = np.random.choice(range(n), p=probs)
                path.append(j)
                visited.add(j)
            path.append(0)
            length = sum(dist_matrix[path[i]][path[i+1]] for i in range(len(path)-1))
            all_paths.append((path, length))
            if length < best_length:
                best_length = length
                best_path = path
        pheromone *= (1 - rho)
        for path, length in all_paths:
            for i in range(len(path)-1):
                pheromone[path[i]][path[i+1]] += q / length
    return best_path, best_length

if __name__ == "__main__":
    coords = np.load("data/coords.npy")
    dist_matrix = calc_distance_matrix(coords)
    n = len(coords)
    path, length = aco_tsp(dist_matrix, n)
    print("蚁群算法路径:", path)
    print("路径长度:", round(length, 2))