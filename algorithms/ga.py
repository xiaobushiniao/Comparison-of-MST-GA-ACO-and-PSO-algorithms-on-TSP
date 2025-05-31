# -*- coding: utf-8 -*-
import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import random
import numpy as np
from utils.distance import calc_distance_matrix

def ga_tsp(dist_matrix, n, population_size=50, generations=200, crossover_rate=0.8, mutation_rate=0.02):
    def create_individual():
        individual = list(range(1, n))
        random.shuffle(individual)
        return [0] + individual + [0]

    def fitness(ind):
        length = sum(dist_matrix[ind[i]][ind[i+1]] for i in range(len(ind)-1))
        return 1 / length

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
        total_fitness = sum(weighted)
        probs = [f / total_fitness for f in weighted]
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
    coords = np.load("data/coords.npy")
    dist_matrix = calc_distance_matrix(coords)
    n = len(coords)
    path, length = ga_tsp(dist_matrix, n)
    print("遗传算法路径:", path)
    print("路径长度:", round(length, 2))