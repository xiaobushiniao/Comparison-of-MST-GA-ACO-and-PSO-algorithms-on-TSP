import numpy as np
import pandas as pd
import time

from utils.distance import calc_distance_matrix
from algorithms.mst import mst_approx_tsp
from algorithms.aco import aco_tsp
from algorithms.ga import ga_tsp
from algorithms.pso import pso_tsp

coords = np.load("data/coords.npy")
dist_matrix = calc_distance_matrix(coords)
n = len(coords)

def brute_force_tsp(dist_matrix):
    from itertools import permutations
    min_path = None
    min_dist = float('inf')
    for perm in permutations(range(1, n)):
        path = [0] + list(perm) + [0]
        dist = sum(dist_matrix[path[i]][path[i+1]] for i in range(len(path)-1))
        if dist < min_dist:
            min_dist = dist
            min_path = path
    return min_path, min_dist

def evaluate_algorithms():
    opt_path, opt_length = brute_force_tsp(dist_matrix)

    start = time.time()
    path1, len1 = mst_approx_tsp(dist_matrix, n)
    time1 = time.time() - start

    start = time.time()
    path2, len2 = aco_tsp(dist_matrix, n)
    time2 = time.time() - start

    start = time.time()
    path3, len3 = ga_tsp(dist_matrix, n)
    time3 = time.time() - start

    start = time.time()
    path4, len4 = pso_tsp(dist_matrix, n)
    time4 = time.time() - start

    results = {
        "算法": ["最小生成树", "蚁群算法", "遗传算法", "微粒群算法"],
        "路径长度": [round(len1, 2), round(len2, 2), round(len3, 2), round(len4, 2)],
        "与最优解差值": [round(len1 - opt_length, 2), round(len2 - opt_length, 2), round(len3 - opt_length, 2), round(len4 - opt_length, 2)],
        "运行时间（秒）": [round(time1, 4), round(time2, 4), round(time3, 4), round(time4, 4)],
    }

    df_result = pd.DataFrame(results)
    print(df_result)

if __name__ == "__main__":
    evaluate_algorithms()
