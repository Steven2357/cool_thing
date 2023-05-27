import numpy as np
from easygui import *
from ip_to_array import *
from det import *
from transpose import *
from reche import *
from inverse import *
from spaces import *
from diagonal import *
from sympy import Rational, Symbol

def renew_input_line():
    global input_line
    input_line=f"""Your Matrixs : {set(matrix_dict.keys())}\n
    0 : Input Data
    1 : Check Data
    2 : Operatation
    3 : Value
    4 : Spaces
    5 : Diagonal\n\n"""



matrix_dict={'0':np.zeros((2,2),dtype=Rational), '1':np.array([[1,0],[0,1]],dtype=Rational)}
Operator=["+","-","*constant","*matrix","transpose","reduce echelon form","inverse"]
Value=["determine","rank","nullity","eigen value and eigen space"]
Spaces=["col","N"]
x=Symbol("x")
renew_input_line()
while True:
    try:
        ip=int(enterbox(input_line+"Your Input: "))
        if ip==0:
            ip=enterbox("The Name Of New Matrix: ")
            matrix_dict[ip]=ip_to_array(ip)
            renew_input_line()
                
        if ip==1:
            ip=choicebox(f"Your Matrices : {set(matrix_dict.keys())}\n"+"The Name Of The Matrix: ","",matrix_dict)
            msgbox(f"{ip} = \n{matrix_dict[ip]}")

        if ip==2:
            ip=enterbox("The Name Of New Or Old Matrix: ")
            A=choicebox("What Do You Want To Calculate?","",matrix_dict)
            op=choicebox(f"{A}","",Operator)
            if op=="+":
                B=choicebox(f"{A} +","",matrix_dict)
                matrix_dict[ip]=matrix_dict[A]+matrix_dict[B]
                msgbox(f"{ip} = {A} + {B} = \n{matrix_dict[ip]}")
            elif op=="-":
                B=choicebox(f"{A} -","",matrix_dict)
                matrix_dict[ip]=matrix_dict[A]-matrix_dict[B]
                msgbox(f"{ip} = {A} - {B} = \n{matrix_dict[ip]}")
            elif op=="*constant":
                B=Rational(enterbox(f"{A} *"))
                matrix_dict[ip]=matrix_dict[A]*B
                msgbox(f"{ip} = {A} * {B} = \n{matrix_dict[ip]}")
            elif op=="*matrix":
                B=choicebox(f"{A} *","",matrix_dict)
                matrix_dict[ip]=np.zeros((matrix_dict[A].shape[0],matrix_dict[B].shape[1]))
                for i in range(matrix_dict[A].shape[0]):
                    for j in range(matrix_dict[B].shape[1]):
                        matrix_dict[ip][i][j]=sum(matrix_dict[A][i]*matrix_dict[B][:,j])
                msgbox(f"{ip} = {A} * {B} = \n{matrix_dict[ip]}")
            elif op=="transpose":
                matrix_dict[ip]=transpose(matrix_dict[A])
                msgbox(f"{ip} = transpose({A}) = \n{matrix_dict[ip]}")
            elif op=="reduce echelon form":
                matrix_dict[ip]=reche(matrix_dict[A])
                msgbox(f"{ip} = reduce echelon form({A}) = \n{matrix_dict[ip]}")
            elif op=="inverse":
                matrix_dict[ip]=inverse(matrix_dict[A])
                msgbox(f"{ip} = inverse({A}) = \n{matrix_dict[ip]}")

            renew_input_line()

        if ip==3:
            op=choicebox("What Do You Want To Calculate?","",Value)
            if op=="determine":
                A=choicebox("det()","",matrix_dict)
                msgbox(f"det({A}) = {det(matrix_dict[A])}")
            elif op=="rank":
                A=choicebox("rank()","",matrix_dict)
                msgbox(f"rank({A}) = {rank(matrix_dict[A])}")
            elif op=="nullity":
                A=choicebox("nullity()","",matrix_dict)
                msgbox(f"nullity({A}) = {nullity(matrix_dict[A])}")
            elif op=="eigen value and eigen space":
                A=choicebox("eigen value and eigen space()","",matrix_dict)
                ouput=""
                for num in eigen_values(matrix_dict[A]):
                    ouput+=f"lamda = {num}, E({A}) = span({eigen_space(matrix_dict[A],num)})\n"
                msgbox(ouput)
                del ouput

        if ip==4:
            op=choicebox("What Do You Want To Calculate?","",Spaces)
            if op=="col":
                A=choicebox("col()","",matrix_dict)
                msgbox(f"col({A}) = span{col(matrix_dict[A])}")
            if op=="N":
                A=choicebox("N()","",matrix_dict)
                msgbox(f"N({A}) = span{N(matrix_dict[A])}")

        if ip==5:
            A=choicebox("diagonal()","",matrix_dict)
            D,U=diagonal(matrix_dict[A])
            U_inverse=inverse(U)
            msgbox(f"""{A} = (U)(D)(U_inverse) = 
{matrix_dict[A]}
U = 
{U}
D = 
{D}
U_inverse = 
{U_inverse}""")
        

            
    except:
        msgbox("ERROR!!!")