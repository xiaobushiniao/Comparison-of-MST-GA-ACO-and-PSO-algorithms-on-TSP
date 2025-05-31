# -*- coding: utf-8 -*-
import sys
import os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import networkx as nx
import numpy as np
from utils.distance import calc_distance_matrix

def mst_approx_tsp(dist_matrix, n):
    G = nx.Graph()
    for i in range(n):
        for j in range(i + 1, n):
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
    coords = np.load("data/coords.npy")
    dist_matrix = calc_distance_matrix(coords)
    n = len(coords)
    path, length = mst_approx_tsp(dist_matrix, n)
    print("最小生成树算法路径:", path)
    print("路径长度:", round(length, 2))