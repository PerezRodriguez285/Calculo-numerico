# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 17:27:39 2020

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Calculo Numerico
TEMA: Raices de una ecuacion lineal
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesor: Mtro. Manuel Almeida Vazquez
Descripción: Muestra la ecuacion usando metodo grafico

"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import linspace, sin, cos, exp, pi
x=linspace(0,2*pi,100)

y=2*cos(x)

figure, ax=plt.subplots()
ax.plot(x,y)

ax.grid()
ax.set_title('Metodo grafico')

plt.show()
#plt.save('met_graf_01.jpg)