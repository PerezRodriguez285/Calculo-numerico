# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 19:53:45 2020

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Calculo Numerico
TEMA: Raices de una ecuacion lineal
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesor: Mtro. Manuel Almeida Vazquez
Descripción: Ejercicio de una reiz cubica resuelta y mostrando su 
             resultado a partir del metodo grafico

"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import linspace, sin, cos, exp, pi

fx = lambda x: x**3 + 4*x**2 - 10 
a=1
b=2
tolera = 0.001

tramo = b-a

while not(tramo<tolera):
    c=(a+b)/2
    fa=fx(a)
    fb=fx(b)
    fc=fx(c)
    cambia = np.sign(fa)*np.sign(fc)
    if cambia < 0:
        a=a
        b=c
    if cambia > 0:
        a=c
        b=b
    tramo = b-a

figure, ax=plt.subplots()

plt.plot(a,b)
plt.plot(a,b,'o')
plt.axhline(0, color="black")
ax.plot(a, b)
ax.grid()
ax.set_title('Metodo grafico')
plt.show()
 
print('       raiz en: ', c)
print('error en tramo: ', tramo)


#plt.save('met_graf_02.jpg')