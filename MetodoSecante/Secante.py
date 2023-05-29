# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 17:38:59 2020

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Calculo Numerico
TEMA: Metodo de la secante
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesor: Mtro. Manuel Almeida Vazquez
Descripción: 
"""

def poli(x):
    y = pow(x,2)-3.8*x-4
    return (y)

print('====================================')
print('======Metodo de la secante==========')
print('====================================')

x1 = float(input('Introduce el valor de inicio x1: '))
x0 = float(input('Introduce el valor de inicio x0: '))
erroru = float(input('Introduce el error '))
raiz = []

raiz.insert(0,0)
i=0
error=1.0
#x2=int(1)

while abs(error) > erroru:
    x2 = x1 - (poli(x1)*(x1-x0))/(poli(x1)-poli(x0))
    raiz.append(x2)
    x0 = x1
    x1 = x2

    error=(raiz[i]-raiz[i-1])/raiz[i]
    print("el valor de la raiz es: ",x2)
    print(x2)
    
