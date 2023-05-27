#UNDONE
import numpy as np
from sympy import Rational, Symbol, factor, solveset
from det import *

x=Symbol("x")

def CRP(A0=np.array([[1,0],[0,1]])):
    A=A0.copy()
    for i in range(A.shape[0]):
        A[i,i]-=x
    return factor(det(A))

def eigen_value(A=np.array([[1,0],[0,1]])):
    crp=CRP(A)
    sol=solveset(crp)
    if "I" in str(sol):
        raise
    return list(sol)    

print(eigen_value(np.array([[0,1],[-1,0]],dtype=Rational)))