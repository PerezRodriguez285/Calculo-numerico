# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 12:38:38 2020

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Calculo Numerico
TEMA: Metodo de Gauss-seidel
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesor: Mtro. Manuel Almeida Vazquez
Descripción:
"""

import numpy as np
from numpy import linalg
import math
import os
import aux_jac as aj
os.system("cls")
print('====================================')
print('=======Metodo de Gauss-Seidel=======')
print('====================================')
it=int(input('De el numero de iteraciones: '))
#Ejercicio 1


A=np.array( [ [22.0, -2.0, 3.0, -1.0],
             [4.0, -32.0, -1.0, -3.0],
             [2.0,-1.0, 45.0, 1.0 ],
             [3.0, -6.0, -8.0, -32.0]] ,dtype=float)

ren,col=np.shape(A)
print(A)
T=np.zeros((ren,col),dtype=float)
T=-A
k=int(1)
cont=0
X0=np.zeros((ren,1) ,dtype=float)
X1=np.zeros((ren,1),dtype=float)
B=np.array([[-610.0],[-420.0],[342.0],[98.0]])
b=np.zeros((ren,1),dtype=float)
t=np.zeros((ren,1),dtype=float)
print(B)
tol=pow(10,-5)
err=1.0
if  __name__=="__main__":
	print("=============Verificando Dominancia:===========")
	if (aj.domina(A)):
		T,b=aj.const(T,A,B,b)
		print (T)
		print(b)
		print('========================')
		print("Ejecutando iteraciones")
		while k<it or err>tol:
			for i in range(ren):
					X1[i]=b[i]+T[i,:]@X0
					X0[i]=X1[i]
			err=linalg.norm(X1-X0)
			k +=1
		print("================== Se llego a la solucion===========")
		print("================== en la iteracion :===========",k)
		print("===============y un error de :===========",err)
		print(X0)
		print("=============El vector residual es: ===========")
		print(B-(A@X0))
	else:
		print("El sistema no converge")
			
	




 

