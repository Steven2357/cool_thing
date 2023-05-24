import numpy as np
from easygui import *
from ip_to_array import *
from det import *

def renew_input_line():
    global input_line
    input_line=f"""Your Matrixs : {set(matrix_dict.keys())}\n
    0 : Input Data
    1 : Check Data
    2 : Operatation
    3 : Value\n\n"""



matrix_dict={'0':np.zeros((2,2)), '1':np.array([[1,0],[0,1]])}
Operator=["+","-","*constant","*matrix"]
Value=["determine","rank"]
renew_input_line()
while True:
    #try:
    ip=int(enterbox(input_line+"Your Input: "))
    if ip==0:
        ip=enterbox("The Name Of New Matrix: ")
        matrix_dict[ip]=ip_to_array(ip)
        renew_input_line()
            
    if ip==1:
        ip=choicebox(f"Your Matrices : {set(matrix_dict.keys())}\n"+"The Name Of The Matrix: ","",matrix_dict)
        msgbox(matrix_dict[ip])

    if ip==2:
        ip=enterbox("The Name Of New Or Old Matrix: ")
        A=choicebox("What Do You Want To Calculate?","",matrix_dict)
        op=choicebox(f"{A}","",Operator)
        if op=="+":
            B=choicebox(f"{A} +","",matrix_dict)
            matrix_dict[ip]=matrix_dict[A]+matrix_dict[B]
            msgbox(f"{ip} = {A} + {B} = {matrix_dict[ip]}")
        elif op=="-":
            B=choicebox(f"{A} -","",matrix_dict)
            matrix_dict[ip]=matrix_dict[A]-matrix_dict[B]
            msgbox(f"{ip} = {A} - {B} = {matrix_dict[ip]}")
        elif op=="*constant":
            B=float(enterbox(f"{A} *"))
            matrix_dict[ip]=matrix_dict[A]*B
            msgbox(f"{ip} = {A} * {B} = {matrix_dict[ip]}")
        elif op=="*matrix":
            B=choicebox(f"{A} *","",matrix_dict)
            matrix_dict[ip]=np.zeros((matrix_dict[A].shape[0],matrix_dict[B].shape[1]))
            for i in range(matrix_dict[A].shape[0]):
                for j in range(matrix_dict[B].shape[1]):
                    matrix_dict[ip][i][j]=sum(matrix_dict[A][i]*matrix_dict[B][:,j])
            msgbox(f"{ip} = {A} * {B} = {matrix_dict[ip]}")

        renew_input_line()

    if ip==3:
        op=choicebox("What Do You Want To Calculate?","",Value)
        if op=="determine":
            A=choicebox("det()","",matrix_dict)
            msgbox(f"det({A})={det(matrix_dict[A])}")
        

            
#except:
    #msgbox("ERROR!!!")