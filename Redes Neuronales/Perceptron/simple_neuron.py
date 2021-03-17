#
import math

e1 = 1
e2 = 1

weigth1 = 0.9812
weigth2 = 3.7193

bias = 2.1415


output = (e1*weigth1+e2*weigth2+bias)
#print output

#tambien se puede expersa como lista

inputs = [1,1]
weigths = [0.9812,-3.7193]
bias = 2.1415
output1 = 0
a=0

#output_with_lists = (inputs[0]*weigths[0])
for i in inputs:

	output1 += i*weigths[a] 
	a+=1
output1 = output1+bias
#print output1
print (1) if output1>0 else 0




#S = f ( E1 * P1 + E2 * P2 + 1 * P3 )
#Y que es f( ) una funcion que podria implementarse asi:
#Funcion f(valor)
#Inicio
#Si valor > 0 entonces
#retorne 1
#de lo contrario
#retorne 0
#fin si
#Fin

#Intento de traduccion lo de C# xdxdxd

import random
import time

def Perceptron_Simple():

	datos = [[1,1,1],[1,0,0],[0,1,0],[0,0,0]]#x1,x2,y --> verdadero, verdadero, verdadero; verdader, falso, falso
	#AND check si en ambas tabla contienen 1 --> [1,1,verdadero],[1,0,falso],[0,1,falso],[0,0,falso]
	# OR checkear si en la tabla hay un 1 --> [1,1,verdadero],[1,0,verdadero],[0,1,verdadero],[0,0,falso]
	#XOR checkear si en la tabla hay un 1 y un 0 --> [1,1,falso],[1,0,verdadero],[0,1,verdadero],[0,0,falso]
	# El preceptron simple no peude evaluar un xor

	pesos = [random.random(),random.random(),random.random()]
	#pesos[2] = bias
	aprendiendo = True

	salida,iteracion = 0,0
	tasaAprende = 0.3
	print ('*** Buscando ***')
	while aprendiendo:
		
		iteracion+=1
		aprendiendo = False
		for cont in range(0,4):
			
			salidaReal = datos[cont][0]*pesos[0]+datos[cont][1]*pesos[1]+pesos[2]
			#print salidaReal
			salida = 1 if salidaReal>0 else 0
			error = datos[cont][2]-salida

			if error!=0:#Cambiar al azar si no coincide. pero en este caso es con la formula de Rosenblatt 
				
				pesos[0] += tasaAprende*error*datos[cont][0]
				pesos[1] += tasaAprende*error*datos[cont][1]
				pesos[2] += tasaAprende*error*1
				aprendiendo = True
		#if iteracion>1002:
			##print 'limite excedido. Mas de 1000 iteraciones sin exito'
			#break

	print ('iteraciones: {}\npeso1: {} \npeso2: {} \npeso3: {}'.format(iteracion,pesos[0],pesos[1],pesos[2]))

	for cont in range(0,4):
		salidaReal = datos[cont][0]*pesos[0]+datos[cont][1]*pesos[1]+pesos[2]
		salida = 1 if salidaReal >0 else 0
		print ('Entradas: {} y {} = {}    perceptron: {}'.format(datos[cont][0],datos[cont][1],datos[cont][2],salida))
Perceptron_Simple()







'''
import turtle

SPEED = 5
BG_COLOR = "blue"
PEN_COLOR = "lightgreen"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
DRAWING_WIDTH = 700
DRAWING_HEIGHT = 700
PEN_WIDTH = 5
TITLE = "H-Tree Fractal with Python Turtle Graphics"
FRACTAL_DEPTH = 3


def draw_line(tur, pos1, pos2):
    # print("Drawing from", pos1, "to", pos2)  # Uncomment for tracing the algorithm.
    tur.penup()
    tur.goto(pos1[0], pos1[1])
    tur.pendown()
    tur.goto(pos2[0], pos2[1])


def recursive_draw(tur, x, y, width, height, count):
    draw_line(
        tur,
        [x + width * 0.25, height // 2 + y],
        [x + width * 0.75, height // 2 + y],
    )
    draw_line(
        tur,
        [x + width * 0.25, (height * 0.5) // 2 + y],
        [x + width * 0.25, (height * 1.5) // 2 + y],
    )
    draw_line(
        tur,
        [x + width * 0.75, (height * 0.5) // 2 + y],
        [x + width * 0.75, (height * 1.5) // 2 + y],
    )

    if count <= 0:  # The base case
        return
    else:  # The recursive step
        count -= 1
        # Top left
        recursive_draw(tur, x, y, width // 2, height // 2, count)
        # Top right
        recursive_draw(tur, x + width // 2, y, width // 2, height // 2, count)
        # Bottom left
        recursive_draw(tur, x, y + width // 2, width // 2, height // 2, count)
        # Bottom right
        recursive_draw(tur, x + width // 2, y + width // 2, width // 2, height // 2, count)


if __name__ == "__main__":
    # Screen setup
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title(TITLE)
    screen.bgcolor(BG_COLOR)

    # Turtle artist (pen) setup
    artist = turtle.Turtle()
    artist.hideturtle()
    artist.pensize(PEN_WIDTH)
    artist.color(PEN_COLOR)
    artist.speed(SPEED)

    # Initial call to recursive draw function
    recursive_draw(artist, - DRAWING_WIDTH / 2, - DRAWING_HEIGHT / 2, DRAWING_WIDTH, DRAWING_HEIGHT, FRACTAL_DEPTH)

    # Every Python Turtle program needs this (or an equivalent) to work correctly.
    turtle.done()'''