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

def Somme_2_Mat_boucle(M,N):
    nmb_lines_M = nombre_lignes_Mat(M)
    nmb_columns_M = nombre_colonnes_Mat(M)
    nmb_lines_N = nombre_lignes_Mat(N)
    nmb_columns_N = nombre_colonnes_Mat(N)
    if((nmb_lines_M == nmb_lines_N) and (nmb_columns_M == nmb_columns_N)):
        for i in range(nmb_lines_M):
            for j in range(nmb_columns_N):
                A[i][j] = M[i][j] + N[i][j]
        return np.array(A)
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

    return np.array(NewMat)

def transpose_Mat_mxn(A):
    """Transposition d'une matrice de taille MxN avec des boucles

    Args:
        A (list of lists): Matrice de taille MxN (listes imbriquées)

    Returns:
        list of lists: Matrice A transposée
    """
    # Nombre de lignes et de colonnes de A
    nmb_line_A = nombre_lignes_Mat(A)
    nmb_col_A = nombre_colonnes_Mat(A)

    # Création d'une matrice vide de taille NxM pour la transposition
    MatriceR = [[0] * nmb_line_A for _ in range(nmb_col_A)]  # Liste imbriquée, remplie de zéros

    # Transposition proprement dite
    for i in range(nmb_line_A):
        for j in range(nmb_col_A):
            MatriceR[j][i] = A[i][j]
    
    return np.array(MatriceR)
