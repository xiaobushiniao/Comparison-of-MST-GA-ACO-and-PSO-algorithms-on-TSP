
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

def ga_tsp(dist_matrix, population_size=50, generations=200, crossover_rate=0.8, mutation_rate=0.02):
    def create_individual():
        individual = list(range(1, n))
        random.shuffle(individual)
        return [0] + individual + [0]

    def fitness(ind):
        return 1 / sum(dist_matrix[ind[i]][ind[i+1]] for i in range(len(ind)-1))

    def crossover(p1, p2):
        start, end = sorted(random.sample(range(1, n), 2))
        child = [-1] * (n+1)
        child[start:end] = p1[start:end]
        ptr = end
        for gene in p2[1:n]:
            if gene not in child:
                if ptr == n:
                    ptr = 1
                child[ptr] = gene
                ptr += 1
        child[0], child[-1] = 0, 0
        return child

    def mutate(ind):
        a, b = sorted(random.sample(range(1, n), 2))
        ind[a], ind[b] = ind[b], ind[a]

    population = [create_individual() for _ in range(population_size)]
    best = min(population, key=lambda ind: sum(dist_matrix[ind[i]][ind[i+1]] for i in range(len(ind)-1)))
    best_length = sum(dist_matrix[best[i]][best[i+1]] for i in range(len(best)-1))

    for _ in range(generations):
        weighted = [fitness(ind) for ind in population]
        probs = [f/sum(weighted) for f in weighted]
        new_pop = []
        while len(new_pop) < population_size:
            p1, p2 = random.choices(population, weights=probs, k=2)
            child = crossover(p1, p2) if random.random() < crossover_rate else p1.copy()
            if random.random() < mutation_rate:
                mutate(child)
            new_pop.append(child)
        population = new_pop
        current_best = min(population, key=lambda ind: sum(dist_matrix[ind[i]][ind[i+1]] for i in range(len(ind)-1)))
        current_length = sum(dist_matrix[current_best[i]][current_best[i+1]] for i in range(len(current_best)-1))
        if current_length < best_length:
            best, best_length = current_best, current_length
    return best, best_length

if __name__ == "__main__":
    path, length = ga_tsp(dist_matrix)
    print("GA Path:", path)
    print("GA Length:", round(length, 2))
