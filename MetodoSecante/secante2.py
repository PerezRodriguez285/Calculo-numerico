"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Calculo Numerico
TEMA: Metodo del punto fijo
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesor: Mtro. Manuel Almeida Vazquez
Descripción: Programa usado para mi examen
"""
import numpy as np
import matplotlib.pyplot as mp 
from numpy import linspace, sin, cos, exp, pi
import math
import os
import f

os.system("cls")
print('============================')
print('====METODO DE LA SECANTE=====')
print('====Funcion==================')
print('====en modulo f.py=====')
print('============================')

a=float(input('De la aproximacion inicial a: '))
a1=a
b=float(input('De la aproximacion inicial b: '))
b1=b
tol=float(pow(10,-5))
max_it=float(100.0)

contador=2

q0= f.f0(a)
q1= f.f0(b)

print('\n Calculando la raiz')
print('it \t a \t b \t x1 \t err')

while(contador<max_it):
    x1 = b - q1*((b-a)/(q1-q0))
    err=np.linalg.norm(x1-b)
   
    if( abs(x1-b) < tol or err < tol  ):
        print('la raiz es: ',x1)
        break
    print(contador ,'\t',a,'\t',b,'\t',x1,'\t',err)
    contador=contador+1
    a=b
    q0=q1
    b=x1
    q1=f.f0(x1)
if(contador>max_it):
    print('El metodo fracasó despues de',max_it,' iteraciones')

x=np.linspace(a1,b1,100)
y1=(f.f0)(x)
figure, ax = mp.subplots()
ax.plot(x,y1)
ax.grid()
mp.show()
