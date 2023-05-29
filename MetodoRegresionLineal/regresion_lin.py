# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 15:49:50 2020

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Calculo Numerico
TEMA: Metodo de regresion lineal
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesor: Mtro. Manuel Almeida Vazquez
Descripción: Funcion lineal
"""

import numpy as np
import matplotlib.pyplot as mp
import gauss_grad
import os

#os.system("Clear")
print("\n\tMetodo de regresion lineal\n")
print("Primero con formulas de las ecuaciones normales\n")
X = np.array([2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6])
Y = np.array([-0.012, -0.19, 0.452, 0.37, 0.764, 0.532, 1.073, 1.286, 1.502, 1.582, 1.993, 2.473])
xp = np.array([2.5, 3.5, 4.5, 5.2])
n = np.size(X)
print(n)

XB = np.mean(X)
YB = np.mean(Y)
SX = np.sum(X)
SY = np.sum(Y)

x2 = X.dot(X)
SX2 = np.sum(x2)
xy = X.dot(Y)
SXY = np.sum(xy)

M = ((YB * SX) - SXY) / (XB * SX - SX2)
print("La pendiente es: ", M)

b = YB - (XB * M)
print("La ordenada es: ", b)

Z = (M * X) + b
print("\nAhora utilizando la matiz del sistema")

A = np.array([ [n, SX, SY], [SX, SX2, SXY]])
print(A)

x0 = gauss_grad.gauss(A)
print(x0)

########################## Para hacer pronosticos ##########################

Z1 = x0[1] * xp + x0[0]
print(Z1)

figure, ax = mp.subplots()
ax.plot(X, Y)
ax.plot(X, Z)
ax.plot(xp, Z1)
ax.grid()
mp.show()