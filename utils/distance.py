import numpy as np

def calc_distance_matrix(coords):
    return np.linalg.norm(coords[:, None, :] - coords[None, :, :], axis=-1)
