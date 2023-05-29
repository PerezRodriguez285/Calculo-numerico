# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 15:51:20 2020

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Calculo Numerico
TEMA: Metodo de regresion lineal y polimonial
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesor: Mtro. Manuel Almeida Vazquez
Descripción: Usando el gradiente de Gauss para resolver problemas de ambos programas
"""

import numpy as np

def gssg(A, b):

    x0 = np.zeros((2, 1))
    x1 = np.zeros((2, 1))
    r = np.copy(b)
    rt = np.transpose(r)
    
    nit = int(25)
    k = int(0)
    err = float(1.0)
    tol = pow(10, -5)
    
    while(k < nit and err > tol):
        
        numera = np.dot(rt, r)
        v1 = np.dot(A, r)
        denom = np.dot(rt, v1)
        alp = numera / denom
        
        x1 = x0 + (alp * r)
        k += 1
        r = np.dot(A, x1) - b
        rt = np.transpose(r)
        x0 = x1
    
    return x0

def gauss(A):
    
    (ren, col) = np.shape(A)
    print(A)
    X = np.zeros((ren, 1))
    S = 0.0
    mg = 0.0
    
    for i in range(0, ren):
        for j in range(i + 1, col - 1):
            mg = A[j][i] / A[i][i]
            A[j, :] = A[j, :] - mg * A[i,:]
    X[ren - 1] = A[ren - 1, col - 1] / A[ren - 1, ren - 1]
    for i in range(ren - 2, -1, -1):
        for j in range(ren - 2, -1, -1): 
            S = S + X[j + 1] * A[i, j + 1]
        X[i] = (A[i, col - 1] - S) / A[i, i]
        S = 0.0
        
    return(X)
   