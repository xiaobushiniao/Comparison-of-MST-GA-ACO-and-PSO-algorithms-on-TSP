
import numpy as np
import random
import time
from itertools import permutations

# 城市坐标
coords = np.array([
    [30, 40],
    [37, 52],
    [49, 49],
    [52, 64],
    [20, 26],
    [40, 30],
    [21, 47],
    [17, 63],
    [31, 62],
    [52, 33],
])
n = len(coords)

# 计算距离矩阵
def calc_distance_matrix(coords):
    return np.linalg.norm(coords[:, None, :] - coords[None, :, :], axis=-1)

dist_matrix = calc_distance_matrix(coords)

def aco_tsp(dist_matrix, num_ants=20, num_iterations=100, alpha=1.0, beta=5.0, rho=0.1, q=1.0):
    pheromone = np.ones_like(dist_matrix)
    best_length = float('inf')
    best_path = None
    for it in range(num_iterations):
        all_paths = []
        for _ in range(num_ants):
            path = [0]
            visited = set(path)
            for _ in range(n-1):
                i = path[-1]
                probs = [(pheromone[i][j] ** alpha) * ((1.0 / dist_matrix[i][j]) ** beta) if j not in visited else 0 for j in range(n)]
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
    path, length = aco_tsp(dist_matrix)
    print("ACO Path:", path)
    print("ACO Length:", round(length, 2))
