# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:11:46 2020

@author: Antonio Alberto de la Luz Perez Rodriguez
"""

import numpy as np
import math
from numpy import linspace, sin, cos, exp, pi

f0=lambda x: exp(x)-1
fp=lambda x: exp(x)

#f0= lambda x: pow(x,4) - 10*pow(x,3) + 35*pow(x,2)-50*x+24
#fp= lambda x: 4*pow(x,3)-30*pow(x,2)+70*x-50

#Problema 5 
#Calcule el minimo de la funcion f(x)=x2+3x-5 usando el metodo de Newton
#f0= lambda x: pow(x,2) + 3*x - 5
#fp= lambda x: 2*x + 3




#Problema 1 raices del polinomio p(x)#
#f0=lambda x:  pow(x,4)-10*pow(x,3)+18*pow(x)-5
#fp=lambda x: 27 * pow(x,2)-10*x+18

#Ejercicio 12
#f0=lambda x: 0.5*pow(x,3)-4*pow(x,2)+5.5*x-1
#fp=lambda x: 1.5*pow(x,2)-8*x+5.5

#Ejercicio 11
#f0=lambda x: -0.9*pow(x,2)+1.7*x+2.5
#fp=lambda x: -1.8*x+1.7*x

#Ejercicio 10
#f0=lambda x: 2*pow(x,3)-11.7*pow(x,2)+17.7*x-5
#fp=lambda x: 6*pow(x,2)-23.4*x+17.7

#Ejercicio 9
#f0=lambda x: pow(x,3)-6*pow(x,2)+11*x-6.1
#fp=lambda x: 3*pow(x,2)-12*x+11

#Ejercicio 8
#f0=lambda x: exp(-0.5*x)*(4-x)-2
#fp=lambda x: 0.5*exp(-0.5*x)*x-3*exp(-0.5*x)

#Ejercicio 7
#f0=lambda x: pow(x,10)-1
#fp=lambda x: 10 * pow(x,9)

#Ejercicio 6
#f0=lambda x: sin(x)+cos(1+x**2)-1
#fp=lambda x: cos(x)-sin(1+x**2)*(2*x)

#Ejercicio 5
#f0=lambda x: pow(x,10)-1
#fp=lambda x: 10 * pow(x,9)

#Ejercicio 4
#f0=lambda x: exp(-x)-x
#fp=lambda x: -exp(-x)-1

#Ejercicio 3
#f0=lambda x: pow(x,6)-8
#fp=lambda x: 6 * pow(x,5)

#Ejercicio 2
#f0=lambda x: pow(x,5)-3
#fp=lambda x: 5 * pow(x,4)

#Ejercicio 1
#f0=lambda x: 9 * pow(x,3)-5*pow(x,2)+18*x-5
#fp=lambda x: 27 * pow(x,2)-10*x+18

