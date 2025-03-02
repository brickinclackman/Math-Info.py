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

def Difference_2_Mat(M,N):
    nmb_lines_M = nombre_lignes_Mat(M)
    nmb_columns_M = nombre_colonnes_Mat(M)
    nmb_lines_N = nombre_lignes_Mat(N)
    nmb_columns_N = nombre_colonnes_Mat(N)
    if((nmb_lines_M == nmb_lines_N) and (nmb_columns_M == nmb_columns_N)):
        A = M - N
        return A
    else:
        print(colored("\n\tIMPOSSIBLE DE CALCULER LA SOMME DE CES DEUX MATRICES","red"))
        return 0
    
def Afficher_Matrice(matrice):
    """Affiche une matrice ligne par ligne."""
    return "\n".join(["[" + " ".join(map(str, ligne)) + "]" for ligne in matrice])

def Mult_2_Mat(M, N):
    # Vérification des dimensions des matrices
    nmb_lines_M = nombre_lignes_Mat(M)
    nmb_columns_M = nombre_colonnes_Mat(M)
    nmb_lines_N = nombre_lignes_Mat(N)
    nmb_columns_N = nombre_colonnes_Mat(N)

    # Vérification de compatibilité des dimensions
    if nmb_columns_M != nmb_lines_N:
        print("\n\tIMPOSSIBLE DE CALCULER LA MULTIPLICATION DE CES DEUX MATRICES")
        return None

    # Initialisation de la nouvelle matrice
    NewMat = [[0 for _ in range(nmb_columns_N)] for _ in range(nmb_lines_M)]

    # Calcul de la multiplication
    for ligne in range(nmb_lines_M):          # Parcourir chaque ligne de M
        for colonne in range(nmb_columns_N):  # Parcourir chaque colonne de N
            for index in range(nmb_columns_M): # Parcourir chaque élément commun
                NewMat[ligne][colonne] += M[ligne][index] * N[index][colonne]

    return NewMat

def transpose_Mat_mxn(A):
    """Transposition d'une matrice de taille MxN avec des boucles

    Args:
        A (np.array): Matrice de taille MxN

    Returns:
        np.array: Matrice A transposée
    """
    nmb_line_A = nmb_line(A)
    #print("Nmb Line A : ",nmb_line_A)
    nmb_col_A = nmb_col(A)
    #print("Nmb Col A : ",nmb_col_A)

    MatriceR = np.zeros((nmb_col_A,nmb_line_A))
    print("MR : ",MatriceR)
    print("A : ",A)
    print("DIM(A) : ",nmb_line_A,"x",nmb_col_A)

    for i in range(nmb_line_A):
        for j in range(nmb_col_A):
            MatriceR[j][i] = A[i][j]
    
    return MatriceR