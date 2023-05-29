# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 11:45:23 2020

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Calculo Numerico
TEMA: Metodo del punto fijo
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
print('======Metodo del punto fijo==========')
print('=====Funcion de iteraciones==========')
print('======en modulo f===============')
print('================================')

x0 = float(input("\nDe el punto inicial de busqueda: "))
it = int(input("\nDe el numero de iteraciones: "))
k = int(1)
tol = float(pow(10, -5))
err = float(5.0)
fc1 = float(125.0)

print("\n\tCalculando Raíz...\n")
print("k \t\t x0 \t\t fc \t\t err")

while(k < it and err > tol):
    
    fc = f.gt(x0)
    err = np.linalg.norm(fc - x0)
    print(k, "\t", x0, "\t", fc, "\t", err)
    
    if(abs(fc1 < fc)):
        
        print("\n\tEstá divergendo u oscilando")
        k = 100
        
    k += 1
    x0 = fc

if(err < tol):
    
    print("La raiz es: " , x0)
    
elif(abs(fc1 < fc)):
    
    print("Esta divergendo u oscilando")
    
graf.graf()