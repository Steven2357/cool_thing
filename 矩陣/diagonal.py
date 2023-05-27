import numpy as np
from sympy import Rational, Symbol, factor, solveset
from det import *
from spaces import *
from transpose import *

x=Symbol("x")

def CRP(A0=np.array([[1,0],[0,1]])):
    A=A0.copy()
    for i in range(A.shape[0]):
        A[i,i]-=x
    return factor(det(A))

def eigen_values(A=np.array([[1,0],[0,1]])):
    crp=CRP(A)
    sol=solveset(crp)
    if "I" in str(sol):
        raise
    return list(sol)

def eigen_space(A0=np.array([[1,0],[0,1]]),landa=0):
    A=A0.copy()
    for i in range(A.shape[0]):
        A[i,i]-=landa
    return N(A)
def diagonal(A=np.array([[1,0],[0,1]])):
    D=np.zeros((A.shape[0],A.shape[1]),Rational)
    U=np.zeros((A.shape[0],A.shape[1]),Rational)
    EVS=eigen_values(A)
    num=0
    for i in range(len(EVS)):
        AM=1
        eq=CRP(A)
        while f"(x - {EVS[i]})" in str(eq/(x-EVS[i])):
            AM+=1
            eq=Rational(eq,(x-EVS[i]))
        GM=len(eigen_space(A,EVS[i]))
        if AM!=GM:
            raise
        for j in range(AM):
            D[num,num]=EVS[i]
            U[num]=eigen_space(A,EVS[i])[j]
            num+=1
    U=transpose(U)
    return D,U