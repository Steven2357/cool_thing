import numpy as np
from sympy import Rational

def reche(A0=np.array([[1,0],[0,1]])):
    A=A0.copy()
    m=A.shape[0]
    n=A.shape[1]
    num=0
    for j in range(n):
        if list(A[:,j])==list(np.zeros((m))):
            continue
        for i in range(num,m):
            if A[i,j]!=0:
                tmp=A[num].copy()
                A[num]=A[i]
                A[i]=tmp
                tmp=A[num,j]
                for j0 in range(n):
                    A[num,j0]=Rational(A[num,j0],tmp)
                num+=1
                break
        for i in range(num,m):
            A[i]+=A[num-1]*(-A[i,j])

    for i in range(m-1,0,-1):
        if list(A[i])==list(np.zeros((n))):
            continue
        for j in range(n):
            if A[i,j]==1:
                for i1 in range(i):
                    A[i1]+=A[i]*(-A[i1,j])
                break

    return A