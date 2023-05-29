import numpy as np
from numpy import linalg
import math
import os
os.system("cls")
print('========================')
print('====Metodo de Jacobi=======')
print('========================')
it=int(input('De el numero de iteraciones: '))
A=np.array( [ [-15.0,2.0,-5.0,10],[9.0,26.0,7.0,-3.0],[12.0,-8.0,31.0,2.0],[-9.0,-5.0,11.0,24.0] ] ,dtype=float)
#A=np.array( [ [7.0,3.0,-1.0,2.0],
            # [3.0,8.0,1.0,-4.0],
             #[-1.0,1.0,4.0,-1.0],
            # [2.0,-4.0,-1.0,6.0] ] ,dtype=float)
ren,col=np.shape(A)
print(A)
T=np.zeros((ren,col),dtype=float)
T=-A
k=int(1)
cont=0
X0=np.zeros((ren,1) ,dtype=float)
print(np.shape(X0))
X1=np.zeros((ren,1),dtype=float)
B=np.array([[-1.0],[0.0],[-3.0],[1.0]])
b=np.zeros((ren,1),dtype=float)
t=np.zeros((ren,1),dtype=float)
print(B)

tol=pow(10,-5)
err=1.0
def domina(A):
	cont=0.0
	S=0.0	
	for i in range(ren):
		S=A.sum(axis=1)
		if (math.fabs(A[i][i]) >=(S[i]-A[i][i])):
			cont +=1
	if(cont != ren):
		print("La matriz no es diagonal dominante")
		return
	else:	
		print("La matriz es diagonal dominante")	
		S=0.0
def const(T,A,B,b):
	for i in range(ren):
		T[i,:]=T[i,:]/A[i,i]
		b[i]=B[i]/A[i,i]
		T[i,i]=0.0

print("=============Verificando Dominancia:===========")
domina(A)
const(T,A,B,b)
print (T)
print(b)
print('========================')
print("Ejecutando iteraciones")
while(k<it or err> tol):
		t=T@X0		
		X1=b+t
		k +=1
		err=np.linalg.norm(X1-X0)			
		X0 = X1	
print("================== Se llego a la solucion:===========")
print("================== en la iteracion:===========",k)
print(X0)




 

