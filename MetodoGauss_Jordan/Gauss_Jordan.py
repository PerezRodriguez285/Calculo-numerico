# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 18:25:55 2020

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Calculo Numerico
TEMA: Metodo de Gauss-Jordan
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesor: Mtro. Manuel Almeida Vazquez
Descripción:
"""

#      --- Importando librerias ---      #
print('===============================================')
print('======Metodo de eliminacion por Gauss==========')
print('==================Jordan=======================')
def mostrarMatriz(matriz,orden):
	for i in range(0,orden):
		linea = "| "
		for j in range(orden+1):
			linea +=  str(matriz[i][j])+" "
		linea += "| "
		print(linea)	
#Ejercicio 1
"""matriz = [[1,2,3,4,5,6,7,8,9,10,10],
          [11,12,13,14,15,16,17,18,19,30,20],
          [21,22,23,24,25,26,27,28,29,40,30],
          [31,32,33,34,35,36,37,38,39,50,40],
          [41,42,43,44,45,46,47,48,49,60,50],
          [51,52,53,54,55,56,57,58,59,70,60],
          [61,62,63,64,65,66,67,68,69,80,70],
          [71,72,73,74,75,76,77,78,79,90,80],
          [81,82,83,84,85,86,87,88,89,100,90],
          [91,92,93,94,95,96,97,98,99,110,100]]"""

matriz = [[4,2,5,60.70],
          [2,5,8,92.90],
          [4,4,3,50.30]]

#Orden de la matriz
orden=len(matriz) 
mostrarMatriz(matriz,orden);    
#Recorrer la matriz 
for j in range(0,orden+1):
	for i in range(0, orden):
		if i>j:
			#Divir los elementos de la matriz
			division=matriz[i][j]/matriz[j][i]
			for k in range(0, orden+1):
				#Obterner el nuevo valor para los elementos en la diagonal inferior
				matriz[i][k]=matriz[i][k]-division*matriz[j][k];
#Recorrer la matriz
#x = [0,0,0,0,0,0,0,0,0,0]
x = [0,0,0]
for i in range(orden,0,-1):
	suma=0
	for j in range(i,orden):
		suma=suma+matriz[i-1][j]*x[j]
	#Obtener los valores de las variables
	x[i-1]=((matriz[i-1][orden]-suma)/matriz[i-1][i-1])	
#Mostrar los valores de las variables
for i in range(0,orden):
	print("x"+str(i)+" = "+str(x[i]))
