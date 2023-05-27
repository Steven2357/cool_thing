#UNDONE
import numpy as np
from reche import *

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
        cols.append(list(A[:,num]))
    return cols

