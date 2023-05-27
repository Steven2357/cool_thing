import numpy as np

def transpose(A=np.array([[1,0],[0,1]])):
    B=np.zeros((A.shape[1],A.shape[0]))
    for i in range(A.shape[1]):
        for j in range(A.shape[0]):
            B[i][j]=A[j][i]
    return B
