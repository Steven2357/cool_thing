import numpy as np

def det(A=np.zeros((2,2))):
    if A.shape[0]!=A.shape[1]:
        raise
    elif A.shape[0]==2:
        return A[0,0]*A[1,1]-A[0,1]*A[1,0]
    else:
        ans=0
        for i in range(A.shape[0]):
            if i==0:
                ans+=A[0,0]*det(A[1:,1:])
            elif i==A.shape[0]-1:
                ans+=A[i,0]*det(A[:i,1:])*(-1)**i
            else:
                ans+=A[i,0]*det(np.vstack((A[:i,1:],A[i+1:,1:])))*(-1)**i
        return ans