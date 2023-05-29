# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 11:11:56 2020

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Calculo Numerico
TEMA: Metodo de regresion polimonial
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesor: Mtro. Manuel Almeida Vazquez
Descripción: Funcion de polinomios
"""

import numpy as np
import matplotlib.pyplot as np
import math
import gauss_grad
import os
os.system("Cls")
print('=========================================================')
print('=======Metodo de regresion Poliomial de 2do grado=======')
print('========================================================')
print('===Forma matricial de las ecuaciones normales===========')

A=np.loadtxt('matA.dat',dtype=float,delimiter=', ',skiprows=0)
print(A)
Y=np.loadtxt('vecty.dat',dtype=float,delimiter=', ',skiprows=0)
print(Y)

At=A.transpose()
M=At@A
print(M)
Ld=At@Y
print(Ld)
N=np.column_stack((M,Ld))
C=gauss_grad.gauss(N)
print("C0= ",C[0])
print("C1= ",C[1])
print("C2= ",C[2])
Z1=C[2]*A[:,2]+C[1]*A[:,1]+C[0]
print(Z1)
figure, ax=np.subplots()
ax.plot(A[:,1],Y)

ax.plot(A[:,1],Z)
ax.grid()
np.show()