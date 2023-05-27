import numpy as np
from sympy import Rational

def reche(A0=np.array([[1,0],[0,1]])):
    A=A0.copy()
    m=A.shape[0]
    n=A.shape[1]
    for j in range(min(m,n)):
        if list(A[:,j])==list(np.zeros((m))):
            continue
        for i in range(j,m):
            if A[i,j]!=0:
                tmp=A[j]
                A[j]=A[i]
                A[i]=tmp
                tmp=A[j,j]
                for j0 in range(n):
                    A[j,j0]=Rational(A[j,j0],tmp)
                break
        for i in range(j+1,m):
            A[i]+=A[j]*(-A[i,j])

    for i in range(m-1,0,-1):
        if list(A[i])==list(np.zeros((n))):
            continue
        for j in range(n):
            if A[i,j]==1:
                for i1 in range(i):
                    A[i1]+=A[i]*(-A[i1,j])
                break

    return A