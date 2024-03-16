import numpy as np

def closest(atoms, v, g):
    v_coords = atoms[v]
    distances = np.linalg.norm(atoms - v_coords, axis=1)
    count = np.sum(distances < g)
    return count
#
atoms = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
v = 0
g = 5
result = closest(atoms, v, g)
print(result)