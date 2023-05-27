import numpy as np
from reche import *
from sympy import Rational

def rank(A=np.array([[1,0],[0,1]])):
    A=reche(A)
    ans=0
    for i in range(A.shape[0]):
        if list(A[i])!=list(np.zeros((A.shape[1]))):
            ans+=1
    return ans

def nullity(A=np.array([[1,0],[0,1]])):
    return A.shape[1]-rank(A)

def col(A=np.array([[1,0],[0,1]])):
    B=reche(A)
    vars=[]
    for i in range(B.shape[0]):
        for j in range(B.shape[1]):
            if B[i,j]==1:
                vars.append(j)
                break
    cols=[]
    for num in vars:
        cols.append(tuple(A[:,num]))
    return tuple(cols)

def N(A=np.array([[1,0],[0,1]])):
    B=reche(A)
    vars=[]
    for i in range(B.shape[0]):
        for j in range(B.shape[1]):
            if B[i,j]==1:
                vars.append(j)
                break

    freevars=list(set([i for i in range(B.shape[1])])-set(vars))
    if freevars==set():
        return tuple()
    Ns=list(np.zeros((len(freevars),B.shape[1]),Rational))
    for i in range(len(freevars)):
        Ns[i][freevars[i]]=Rational(1)
    if vars==[]:
        for i in range(len(Ns)):
            Ns[i]=tuple(Ns[i])
        return tuple(Ns)
    for i in range(len(Ns)):
        for j in range(len(vars)):
            Ns[i][vars[j]]=Rational(-B[j][freevars[i]])
    for i in range(len(Ns)):
        Ns[i]=tuple(Ns[i])
    return tuple(Ns)