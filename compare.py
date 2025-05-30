
from mst import mst_approx_tsp, calc_distance_matrix, coords
from aco import aco_tsp
from ga import ga_tsp
from pso import pso_tsp
from itertools import permutations
import time

dist_matrix = calc_distance_matrix(coords)

def brute_force_tsp(dist_matrix):
    n = len(dist_matrix)
    min_path, min_dist = None, float('inf')
    for perm in permutations(range(1, n)):
        path = [0] + list(perm) + [0]
        dist = sum(dist_matrix[path[i]][path[i+1]] for i in range(len(path)-1))
        if dist < min_dist:
            min_path, min_dist = path, dist
    return min_path, min_dist

opt_path, opt_length = brute_force_tsp(dist_matrix)

start = time.time(); _, len1 = mst_approx_tsp(dist_matrix); t1 = time.time() - start
start = time.time(); _, len2 = aco_tsp(dist_matrix); t2 = time.time() - start
start = time.time(); _, len3 = ga_tsp(dist_matrix); t3 = time.time() - start
start = time.time(); _, len4 = pso_tsp(dist_matrix); t4 = time.time() - start

print(f"最优路径长度: {round(opt_length, 2)}")
print(f"MST: {round(len1, 2)} (Δ{round(len1 - opt_length, 2)}), time: {round(t1, 4)}s")
print(f"ACO: {round(len2, 2)} (Δ{round(len2 - opt_length, 2)}), time: {round(t2, 4)}s")
print(f"GA : {round(len3, 2)} (Δ{round(len3 - opt_length, 2)}), time: {round(t3, 4)}s")
print(f"PSO: {round(len4, 2)} (Δ{round(len4 - opt_length, 2)}), time: {round(t4, 4)}s")
