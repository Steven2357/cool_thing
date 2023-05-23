import numpy as np
from easygui import *

def ip_to_array(N="N"):
    Ip=[]
    ip=""
    while True:
        ip=enterbox(f"{N} = ",N)
        if ip=="":
            break
        Ip.append(ip)
    Ipp=[]
    lenIpp=[]
    for item in Ip:
        tmp=item.split()
        for i in range(len(tmp)):
            tmp[i]=float(tmp[i])
        Ipp+=tmp
        lenIpp.append(len(tmp))
    A=np.array(Ipp)
    if lenIpp==[]:
        return 
    len0=lenIpp[0]
    A=A.reshape(-1,len0)
    msgbox(f"{N} = {A}")
    return A