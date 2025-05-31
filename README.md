# Comparison of MST GA ACO and PSO algorithms on TSP
 An analysis and comparison of each algorithm in terms of TSP path length, difference from optimal solution, runtime (seconds), stability, and convergence speed.

## Directory Description

### `data/`
- **`coords.npy`**: City coordinate data file

### `utils/`
- **`distance.py`**: Common distance matrix calculation functions

### `algorithms/`
- **`mst.py`**: Minimum Spanning Tree algorithm implementation
- **`aco.py`**: Ant Colony Optimization algorithm implementation
- **`ga.py`**: Genetic Algorithm implementation
- **`pso.py`**: Particle Swarm Optimization algorithm implementation

### Root Directory
- **`compare.py`**: Main comparison program that calls all four algorithm modules




## Path Quality

- **Ant Colony Optimization (ACO)**: Achieves the closest approximation to the optimal solution (154.35) with a difference of 0, demonstrating the **best performance**.

- **Particle Swarm Optimization (PSO)**: Shows a path length of 28.28, but this may be due to non-convergence under certain parameter settings, resulting in **anomalous results**.

- **Genetic Algorithm (GA)**: Produces a path length of 171.62, **ranking second** after ACO.

- **Minimum Spanning Tree (MST)**: Yields a path length of 191.99, which is **fast but considerably distant** from the optimal solution.

## Runtime Performance

- **MST Method**: Extremely short runtime at only **0.0006 seconds**

- **PSO Algorithm**: Relatively fast execution time of **0.1270 seconds**

- **GA Algorithm**: Moderate execution time of **0.2747 seconds**

- **ACO Algorithm**: Requires considerably longer time (**1.0354 seconds**), suitable for scenarios where higher path quality is prioritized

## Stability and Convergence Speed

- **MST Method**: 
  - High stability and fast convergence speed
  - Poor path quality

- **ACO and GA Algorithms**: 
  - Good stability with moderate convergence speeds
  - Suitable for more complex optimization problems
