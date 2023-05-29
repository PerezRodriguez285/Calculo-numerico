# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 12:52:32 2020

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Calculo Numerico
TEMA: Metodo del punto fijo
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesor: Mtro. Manuel Almeida Vazquez
Descripción: Funcion que muestra las graficas de las funciones
"""

import numpy as np
import matplotlib.pyplot as plt
import f

def graf():
    
    x1 = np.linspace(1, 5, 100)
    x2 = np.linspace(1, 5, 100)
    y = f.gt(x1)
    y1 = f.ld(x1)
    y2 = f.f0(x2)
    
    plt.subplot(1, 2, 1)
    plt.plot(x1, y, color = 'blue')
    plt.plot(x1, y1, color = 'green')
    plt.grid()
    
    plt.subplot(1, 2, 2)
    plt.plot(x2, y2, color = 'red')
    plt.grid()
    plt.show()