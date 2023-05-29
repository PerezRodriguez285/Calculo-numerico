# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 12:38:38 2020

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Calculo Numerico
TEMA: Metodo de Jacobi
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesor: Mtro. Manuel Almeida Vazquez
Descripción: Programa auxiliar de la funcion principal
"""
import numpy as np
from numpy import linalg
import math
def domina(A):
	ren,col=np.shape(A)	
	cont=0.0
	S=0.0	
	for i in range(ren):
		S=A.sum(axis=1)
		if (math.fabs(A[i][i]) >=(S[i]-A[i][i])):
			cont +=1
	if(cont != ren):
		print("La matriz no es diagonal dominante")
		return False
	else:	
		print("La matriz es diagonal dominante")		
		return True
	return

def const(T,A,B,b):
	ren,col=np.shape(T)
	for i in range(ren):
		T[i,:]=T[i,:]/A[i,i]
		b[i]=B[i]/A[i,i]
		T[i,i]=0.0
	return T, b
