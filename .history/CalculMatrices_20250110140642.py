import numpy as np
from termcolor import colored

def Create_M_Identity(n):
    i = np.zeros((n,n))
    for index in range(n):
        i[index][index] = 1
    return i

def nombre_lignes_M(M):
    lignes = len(M)
    return lignes

def nombre_colonnes_M(M):
    colonnes = len(M[0])
    return colonnes

def Somme_2_Mat(M,N):
    nmb_lines_M = nombre_lignes(M)
    nmb_columns_M = nombre_colonnes(M)
    nmb_lines_N = nombre_lignes(N)
    nmb_columns_N = nombre_colonnes(N)
    if((nmb_lines_M == nmb_lines_N) and (nmb_columns_M == nmb_columns_N)):
        A = M + N
        #print(colored(f"M + N = \n{A}","green"))
        return A
    else:
        print(colored("\n\tIMPOSSIBLE DE CALCULER LA SOMME DE CES DEUX MATRICES","red"))
        #print(colored(f"lignes : M = {nmb_lines_M}, N = {nmb_lines_N} ; colonnes : M = {nmb_columns_M}, N = {nmb_columns_N}","red"))
        return 0