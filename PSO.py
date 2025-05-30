
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

def pso_tsp(dist_matrix, num_particles=30, iterations=100, w=0.8, c1=1.5, c2=1.5):
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
    path, length = pso_tsp(dist_matrix)
    print("PSO Path:", path)
    print("PSO Length:", round(length, 2))
