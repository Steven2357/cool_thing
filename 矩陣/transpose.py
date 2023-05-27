import numpy as np
from sympy import Rational

def transpose(A=np.array([[1,0],[0,1]])):
    B=np.zeros((A.shape[1],A.shape[0]),Rational)
    for i in range(A.shape[1]):
        for j in range(A.shape[0]):
            B[i][j]=A[j][i]
    return B
