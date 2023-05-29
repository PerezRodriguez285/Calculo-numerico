# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 10:07:03 2020

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Calculo Numerico
TEMA: Metodo de Newton
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesor: Mtro. Manuel Almeida Vazquez
Descripción: 
"""

import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt
import math
import os
import f

os.system("cls")
print('================================')
print('======Metodo de Newton==========')
print('=====Funcion y derivada==========')
print('======en modulo f===============')
print('================================')

x0=float(input('Punto inicial de busqueda: '))
it=int(input('Numero de iteraciones: '))
k=int(1)
tol=float(pow(10,-6))
err=float(5.0)
fc1=float(125.0)
print('Calculando la raiz')
print('k \t\t x0 \t\t\t fc \t\t\t err')
while (k < it and err>tol):
    fc=f.f0(x0)
    fpc=f.fp(x0)
    if fpc==0:
        print('La derivada es igual a cero')
        break
    else:
        x1=x0-(fc/fpc)
        err=np.linalg.norm(x1-x0)
        print(k, '\t',x0, '\t',fc, '\t',err)
        x0=x1
        k +=1
if (abs(fc) < tol or err < tol):
    print("la aproximaion de la raiz es de: ",x0)
else:
    print("Esta divergiendo u oscilando")

x=np.linspace(x0-5,x0+5,100)
y1=(f.f0)(x)
figure, ax=plt.subplots()
ax.plot(x,y1)
ax.grid()
plt.show()