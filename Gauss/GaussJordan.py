# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 12:18:40 2020

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Calculo Numerico
TEMA: Metodo de Gauss-Jordan
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesor: Mtro. Manuel Almeida Vazquez
Descripción:
"""
import numpy as np
import math
import os

print("\n  Metodo de Gauss-Jordan")
print("\n  Matriz aumentada del sistema de ecuaciones:")

A = np.zeros((4, 5), dtype = float)   # Se llena la matriz A de ceros
A = np.loadtxt("matA.m")              # Carga la matriz con los valores que hay en 'matA.m'
(ren, col) = np.shape(A)              # Se obtiene las dimensiones de la matriz
X = np.zeros((ren, 1))                # Se crea la matriz X de tamano renx1

                             
print(A,"\n\n")
#np.set_printoptions(formatter={"float": lambda x:"%0.6f"%(x)})
# PROCEDIMIENTO
# Normalizacion
print(" Gauss-Jordan")
factor = 0.0
for i in range( 0, ren ):
    factor = A[i][i]
    A[i, :] = A[i, :] / factor
    #  elimnacion de renglones
    for j in range( i+1, ren ):
        A[j, :] = A[j, :]- (A[j,i]*A[i, :])
    if(i>0):
        for k in range( 0, i ):
            A[k, :] = A[k, :]- (A[k,i]*A[i, :])       

print(A,"\n")

for i in range( 0, ren ):
    X[i] = A[i, ren]

# Resultados
print("  La solucion es:")
print(X)
