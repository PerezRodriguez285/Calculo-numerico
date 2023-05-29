# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 09:17:55 2020

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Calculo Numerico
TEMA: Metodo de Gauss-Jordan
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesor: Mtro. Manuel Almeida Vazquez
Descripción: Variacion del programa de Gauss_Jordan
"""
import numpy as np

A = np.array([[4,2,5],
              [2,5,8],
              [4,4,3]])

B=np.array([[60.70],
            [92.90],
            [56.30]])

AB = np.concatenate((A,B),axis=1)
AB0 = np.copy(AB)

#Matriz Aumentada
tamano = np.shape(AB)
n = tamano[0]
m = tamano[1]

for i in range(0,n-1,1):
    columna = abs(AB[i:,i])
    dondemax = np.argmax(columna)
    
    if(dondemax !=0):
        temporal=np.copy(AB[i,:])
        AB[dondemax+i,:]=temporal
AB1 = np.copy(AB)

for i in range(0,n-1,1):
    pivote=AB[i,i]
    adelante=i+1
    for k in range(adelante,n,1):
        factor = AB[k,i]/pivote
        AB[k,:]=AB[k,:]-AB[i,:]*factor      
AB2 = np.copy(AB)

#eliminacion
ultfila = n-1
ultcolumna=m-1

i = ultfila
pivote=AB[i,i]
atras = i-1
for k in range(atras,0,-1):
    factor=AB[k,i]/pivote
    AB[k,:]=AB[k,:]-AB[i,:]*factor

print("Matriz aumentada: ")
print(AB0)
print("Pivote: ")
print(AB1)
print("Eliminacion 1: ")
print(AB2)
print("Eliminacion 2:")
print(AB)