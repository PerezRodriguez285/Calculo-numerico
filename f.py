# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:47:54 2020

@author: Antonio Alberto de la Luz Perez Rodriguez
"""

from numpy import linspace, sin, cos, exp, pi
#Ejericio 5 Aproximae la raiz de x3-5x2+15 aplicando el metodo de 
#biseccion en el intervalo[-2,-1]
#f0=lambda x: pow(x,3) -5 * pow(x,2)+15

f0=lambda x: exp(x)-1

#Ejercicio 10
#f0=lambda x: 2*cos(x)+10*pow(x,10)-1

#Ejercicio 9
#f0=lambda x: (0.8-0.3*x)/x

#Ejercicio 8
#f0=lambda x:  pow(x,4)-8 * pow(x,3) -35*pow(x,2)+450*x -1001

#Ejercicio 7
#f0=lambda x: -2.75 * pow(x,3)+ 18 * pow(x,2) -21*x -12

#Ejercicio 6
#f0=lambda x: -2 * pow(x,6)- 1.5 * pow(x,4) +10*x +2

#Ejercicio 5
#f0=lambda x: -8 * pow(x,4)+ 44 * pow(x,3) -90*pow(x,2)+82*x -25

#Ejercicio 4
#f0=lambda x: 5 * pow(x,3)-5*pow(x,2)+6*x-2

#Ejercicio 3
#f0=lambda x: -0.5 * pow(x,2)+2.5*x+4.5

#Ejercicio 2
#f0=lambda x: pow(x,3)-2*sin(x)

#Ejercicio 1
#f0=lambda x: pow(x,3)-3*x+1