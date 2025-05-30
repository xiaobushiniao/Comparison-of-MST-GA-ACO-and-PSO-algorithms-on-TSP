
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

import networkx as nx

def mst_approx_tsp(dist_matrix):
    G = nx.Graph()
    for i in range(n):
        for j in range(i+1, n):
            G.add_edge(i, j, weight=dist_matrix[i][j])
    mst = nx.minimum_spanning_tree(G)
    visited = []
    def dfs(u):
        visited.append(u)
        for v in sorted(mst[u]):
            if v not in visited:
                dfs(v)
    dfs(0)
    visited.append(0)
    length = sum(dist_matrix[visited[i]][visited[i+1]] for i in range(len(visited)-1))
    return visited, length

if __name__ == "__main__":
    path, length = mst_approx_tsp(dist_matrix)
    print("MST Path:", path)
    print("MST Length:", round(length, 2))
