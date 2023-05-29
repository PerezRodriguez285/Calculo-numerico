5
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:22:14 2020

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Calculo Numerico
TEMA: Metodo de Newton-Raphson
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesor: Mtro. Manuel Almeida Vazquez
Descripción: Resolver algunos ejercicios del metodo de newton usando este programa
"""

import numpy as np
import matplotlib.pyplot as mp
import math 
import os
import f

print('=============================')
print('======Metodo de Newton=======')
print('==== Funcion y derivada======')
print('=============================')

x0=float(input('De el punto inicial de busquedad: '))
it=int(input('De el numero de iteraciones: '))
k=int(1)
tol=float(pow(10,-6))
err=float(5.0)
fcl=float(125.0)
print('Calculando la raiz')
print('k \t\t x0 \t\t\t fc \t\t\t err')
while (k < it and err > tol):
    
    fc =f.f0(x0)
    fpc =f.fp(x0)
    if fpc == 0:
        print('La derivada es igual a 0')
        break
    else:
        x1=x0-(fc/fpc)
        err=np.linalg.norm(x1-x0)
        print(k,'\t',x0,'\t',fc,'\t',err)
        x0=x1
        k += 1
if(abs(fc)< tol or err<tol):
    print('La aproximacion a la raiz es: ',x0)
else:
    print("Esta divergiendo u oscilando")
    
x=np.linspace(x0-5,x0+5,100)
y1=(f.f0)(x)
figure, ax =mp.subplots()
ax.plot(x,y1)
ax.grid()
mp.show()