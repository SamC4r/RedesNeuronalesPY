import random
import math
def algo():
	x = 1
	Yini = Ecuacion(x)
	variacion = 1

	while abs(variacion)>0.00001:
		print variacion
		Ysigue = Ecuacion(x+variacion)
		print Ysigue
		if Ysigue>Yini:
			variacion=variacion*-1
			variacion= variacion/10

		else:
			Yini = Ysigue
			x+=variacion
			print 'x {} y {}'.format(x,Yini)
	print 'respuesta {}'.format(x)

def Ecuacion(x):
	return 5*(x**2)-7*x-13

algo()


#Eso deberia funcinoar en C# pero si no usamos sympy xdxdx

from sympy import *
from sympy import symbols,sympify

x = symbols('x')

ec = 5*(x**2)-7*x-13
der_ec = diff(ec,x)
print der_ec
sol = solve(der_ec)
print float(sol[0])



def algoritmo_descenso_gradiente():
	x = random.randrange(-10,10)
	print x
	origen= equation(x)
	variacion =1

	while variacion>0.00001:

		ptomas = equation(x+variacion)
		ptomenos = equation(x-variacion)
		#print ptomas,origen,ptomenos

		if ptomas<origen: #check si ptomas es menor al origen.
			origen = ptomas
			variacion*=.9
			x+=variacion
#En caso negativo
		elif ptomenos < origen:# chekear si pto menos es menor al origen
			origen = ptomenos
			variacion*=.9
			x-=variacion

		else:
			variacion*=.9


	print '\nCoordendas del minimo\tx: {} y: {}\n'.format(round(x,4),round(origen,4))

def equation(x):
	return 0.1*x**6-3*x**2-13





algoritmo_descenso_gradiente()	
