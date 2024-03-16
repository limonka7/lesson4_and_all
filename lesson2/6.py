import numpy as np
def nonzero(A):
    x,y = np.nonzero(A)
    return x[0],y[0]
A=np.zeros((100,100))
A[56,70]=1
print(nonzero(A))
