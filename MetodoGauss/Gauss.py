# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 12:18:40 2020

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Calculo Numerico
TEMA: Metodo de Gauss
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesor: Mtro. Manuel Almeida Vazquez
Descripción:
"""

import numpy as np
import time
import math
import os
os.system("cls")
print('================================')
print('=========Metodo de Gauss==========')
print('=========Las ecuaciones ==========')
print('======estan en la matriz A===============')
print('=========================================')
print('Matriz aumentada del sistema de ecuaciones')
print('')
"""
#Ejercicio 1
A=np.array([[-25.0, 18.0, 13.0, -9.0, 132.0],
            [32.0, 23.0, -12.0, 16.0, 231.0],
            [22.0, 34.0, -19.0, 12.0, 123.0],
            [-4.0, -15.0, 6.0, 4.0, -176.0]])"""
#Ejercicio 2
A=np.array( [ [-15,2.0,-5.0,10],
             [9.0,26.0,7.0,-3.0],
             [12.0,-8.0,31.0,2.0],
             [-9.0,-5.0,11.0,24.0] ] ,dtype=float)
"""
#Ejercicio 3
A=np.array( [ [1.0,-3.0,2],[2.0,5.0,0],[0.0,-1.0,-2] ] ,dtype=float)
#Ejercicio 4
A=np.array( [ [-15,2,4,3],[9,26,7,-3],[12,-5,6,10],[-9,-5,11,24] ] ,dtype=float)
#Ejercicio 5
A=np.array( [ [8.8, 9.5, 9.8, 9.4, 10.0],
            [9.4, 10.1, 9.2, 11.3, 9.4],
             [10.0, 10.4, 7.9, 10.4, 9.8],
             [9.8, 9.5, 8.9, 8.8, 10.6],
             [10.1, 9.5, 9.6, 10.2, 8.9]] ,dtype=float)
#Ejercicio 6
A=np.array( [ [2,8,6,20],
             [4,2,-2,-2],
             [-6.4,10,24],
             [-9,-5,11,24] ] ,dtype=float)
#Ejercicio 7
A=np.array( [ [-15,2.0,-5.0,10],
             [9.0,26.0,7.0,-3.0],
             [12.0,-8.0,31.0,2.0],
             [-9.0,-5.0,11.0,24.0] ] ,dtype=float)
#Ejercicio 8
A=np.array( [ [29.65, 28.55, 28.65, 30.15],
             [30.65, 28.15, 29.85, 29.05],
             [29.65, 30.45, 29.15, 30.45],
             [31.25 29.45 30.15 29.65] ] ,dtype=float)"""

"""A=np.array([[3.0, 2.0],
            [-1.0, 2.0]])"""
(ren,col)=np.shape(A)
X=np.zeros((ren,1))
S=0.0
print(A)
mg=0.0

for i in range(0,ren):
    for j in range(i+1,col-1):
        mg=A[j][i]/A[i][i]
        A[j,:]=A[j,:]-mg*A[i,:]

print(A)
print(" evaluacion retroactiva ")
X[ren-1]=A[ren-1,col-1]/A[ren-1,ren-1]
for i in range(ren-2,-1,-1):
    for j in range(ren-2,-1-1):
        S=S+X[j+1]*A[i,j+1]
        
        X[i]=(A[i,col-1]-S)/A[i,i]
        S=0.0
print('La solucion es: ')
print(X)