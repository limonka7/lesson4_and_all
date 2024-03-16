import numpy as np
def min_indices(arr):
     indices = np.argsort(arr)[:3]
     return indices
arr = np.array([13,2,5,4,1,71])
print(min_indices(arr))