# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 18:27:14 2020

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Calculo Numerico
TEMA:
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesor: Mtro. Manuel Almeida Vazquez
Descripcion: Segundo programa (variacion del primero)
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy import linspace, sin, cos, exp, pi

x=linspace(-pi/2,pi/2,100)

y=2*cos(2*x)-3*sin(x)

figure, ax=plt.subplots()
ax.plot(x, y)

ax.grid()
ax.set_title('Metodo grafico')

plt.show()
#plt.save('met_graf_02.jpg')
