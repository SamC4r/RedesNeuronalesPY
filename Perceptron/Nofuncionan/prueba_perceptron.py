import random,math

capas = 3
neuronas = 5
total_capas_neuronas = [[0,2],[1,2],[2,1]]#Capa;Neurona
total_pesos = 0
total_pesos_por_capa = 0
entradas = [[1,1]]
salida_esperada = [0]
pesos_valores_capa = []
umbrales = []


for a in range(neuronas-total_capas_neuronas[0][1]):
	umbrales+=[random.random()]
print umbrales

for a in range(1,capas+1):

	if a>=capas:
		break
	else:
		total_pesos+=total_capas_neuronas[a][1]*total_capas_neuronas[a-1][1]
		total_pesos_por_capa = total_capas_neuronas[a][1]*total_capas_neuronas[a-1][1]
	print total_pesos,'pesos desde la capa {}'.format(a)
	print total_pesos_por_capa,'pesos para la capa {}'.format(a)

total2 = []
c=0

		
#pesos [[capa,neurona_inicial,neurona_final,valor_random]]
for i in range(capas):
	c+=1
	#print i, 'i'
	if i>=capas-1:
		break
	for b in range(total_capas_neuronas[i][1]):
		#print b , 'b'
		for a in range(total_capas_neuronas[i+1][1]):
			total2 +=[[i,b,a,random.random()]]
			#print b,a, 'para capa {}'.format(i+1)

print total2


print 'total_pesos =',total_pesos
print 'valores de pesos',pesos_valores_capa


####Salidas capas de entradas#####

a1_2 = [0,0]#venir desde la capa 0 y llegar a la neurona 0
salida1 = 0
salida2 = 0
for cont in range(total_pesos):
	
	if total2[cont][0] is 0 and total2[cont][2] is 0:
		salida1 += entradas[0][0]*total2[cont][3]
		print salida1, 'salida1'
		print total2[cont][3],'si'
	
	if total2[cont][0] is 0 and total2[cont][2] is 1:

		print total2[cont][3], ' no'
		salida2 += entradas[0][0]*total2[cont][3]
	
salida1 +=umbrales[0]
salida2 +=umbrales[1]

salida1 = 1/(1+math.exp(-salida1))
salida2 = 1/(1+math.exp(-salida2))

print salida1,'salida capa 1 y llega a neurona 1'
print salida2, 'salida capa 1 y llega a neurona 2'


#####Salidas capa oculta######

salidas = [[0,salida1],[0,salida1]]#[[capa,n_neurona]]

for a in range(1,capas):
	pass#for i in range()




#Para pereceptron con 

'''	
	c.oculta

*	|*	|	*
*	|*	|
	|	|	
	
			salida
entrada
'''

