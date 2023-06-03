# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:45:25 2020

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Calculo Numerico
TEMA: Metodo de biseccion
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesor: Mtro. Manuel Almeida Vazquez
Descripción: Realiza graficas usando el metodo de biseccion
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import linspace, sin, cos, exp, pi
import time
import math
import os
import f

os.system("cls")
print('================================')
print('======Metodo de biseccion=======')
print('================================')

a=float(input('De el extremo izquierdo del intervalo: '))
a1=a
b=float(input('De el extremo derecho del intervalo (a<b): '))
b1=b
it=int(input('De el numero de iteraciones: '))
k=int(0)
tol=float(pow(10,-5))
err=float(1.0)
fa=f.f0(a)
fb=f.f0(b)
print(fa)
print(fb)

if fa*fb>0:
    print('No hay raiz')
else:
    print('Calculando raiz')
    print('it \t a \t b c\t fc') 
    while(k < it):
        k +=1
        c=float((a+b)/2)
        fa=f.f0(a)
        fc=f.f0(c)
        print(k, '\t',a, '\t',b, '\t',c, '\t',fc)
        time.sleep(5)
        if fa*fc >0:
            a=c
        else:
            b=c
        err=abs(fc)
       
    print('a raiz es: ', c)
x=np.linspace(a1, b1,100)
y1=(f.f0)(x)
figure, ax=plt.subplots()
ax.plot(x,y1)
ax.grid()
plt.show()
