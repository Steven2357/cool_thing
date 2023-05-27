import numpy as np
from reche import *
from det import *

def inverse(A=np.array([[1,0],[0,1]])):
    if det(A)==0:
        raise
    I=np.zeros((A.shape[0],A.shape[1]),dtype=Rational)
    for i in range(A.shape[0]):
        I[i,i]=1
    A=np.hstack((A,I))
    return reche(A)[:,A.shape[0]:]