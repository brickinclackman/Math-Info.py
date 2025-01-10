import numpy as np
from termcolor import colored

def Create_M_Identity(n):
    i = np.zeros((n,n))
    for index in range(n):
        i[index][index] = 1
    return i

def nombre_lignes_Mat(M):
    lignes = len(M)
    return lignes

def nombre_colonnes_Mat(M):
    colonnes = len(M[0])
    return colonnes

def Somme_2_Mat(M,N):
    nmb_lines_M = nombre_lignes_Mat(M)
    nmb_columns_M = nombre_colonnes_Mat(M)
    nmb_lines_N = nombre_lignes_Mat(N)
    nmb_columns_N = nombre_colonnes_Mat(N)
    if((nmb_lines_M == nmb_lines_N) and (nmb_columns_M == nmb_columns_N)):
        A = M + N
        return A
    else:
        print(colored("\n\tIMPOSSIBLE DE CALCULER LA SOMME DE CES DEUX MATRICES","red"))
        return 0
    
def Afficher_Matrice(matrice):
    """Affiche une matrice ligne par ligne."""
    return "\n".join(["[" + " ".join(map(str, ligne)) + "]" for ligne in matrice])

def Mult_2_Mat(M,N):
    nmb_columns_M = nombre_colonnes_Mat(M)
    nmb_lines_N = nombre_lignes_Mat(N)
    if(nmb_columns_M == nmb_lines_N):
        NewMat = [nmb_columns_M][nmb_lines_N]
        return NewMat
    else:
        print(colored("\n\tIMPOSSIBLE DE CALCULER LA MULTIPLICATION DE CES DEUX MATRICES","red"))
        return 0

