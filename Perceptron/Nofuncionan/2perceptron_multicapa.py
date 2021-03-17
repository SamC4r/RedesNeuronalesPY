import random
import math
import time

class Perceptron():
#salid de la primera neurona es igual a = a11 = 1*peso1,1
	def __init__(self):
		self.tasaAprende = 0.4
		self.iteraciones = 0
		self.neuronas_totales = 12
		self.entradas = [1,0]
		self.salidas = [[1,0]]
		self.se_quiere = [
			[1,1,0],
			[1,0,1],
			[0,1,1],
			[0,0,0]
		]
		
		self.buscando = True
		self.capas = 4
		self.perceptron = []#entrada,capa,numero neurona, numero de ujmbral, valor,conexiones (numero de neurona a la que se conecta),valor del peso,[[2,1,1,random.random(),2,random.random()]] 
		self.build()
		self.calculaSalida()


	def build(self):
		capas = self.capas
		c=0
		self.n_entradas = 4
		entradas_hacia_neuronas = len(self.se_quiere[0][:2])
		#print entradas_hacia_neuronas, 'entradas'
		neuronas = [entradas_hacia_neuronas,4,4,2]#[a,b] a = capa ; b = neuronas
		self.total_capas_neuronas = []
		self.umbrales = []
		self.salida_de_cada_neurona = []
		for i in range(capas):#para umbral [a,b,c] a = capa, b = neurona c = valor random
			
			neuronas_por_capa = [[i+1,neuronas[i]]]
			self.total_capas_neuronas+=neuronas_por_capa

		for i in range(0,capas):
			
			for a in range(self.total_capas_neuronas[i][1]):
				
				self.umbrales += [[i,a+1,random.random()]]
				


		print 'Valor de umbrales:\n',self.umbrales[2:],'\n\n'
		print self.total_capas_neuronas,'Capas;Neuronas'



		###salida neuronas####



		#Pesos = [a,b,c,d] = a = capa ; b = neurona 1, c = neurona 2 ; d = valor
		#[[1, 2], [2, 4], [3, 4], [4, 2]]
##############PESOS#############
		self.total2 = []
		c=0

		

		for i in range(capas):
			
			#print i, 'i'
			if i>=capas-1:
				break
			for b in range(self.total_capas_neuronas[i][1]):
				#print b , 'b'
				for a in range(self.total_capas_neuronas[i+1][1]):
					c+=1
					self.total2 +=[[c,i,[b],[a],random.random()]] 
					#print b,a, 'para capa {}'.format(i+1)



		print self.total2,'s'


		print '**Cargando Neurona ***\n\n\n'
		time.sleep(2)

		for a in range(self.n_entradas):
			print 'Entrada {} = {}    Dato esperado = {}'.format(a,self.se_quiere[a][:2],self.se_quiere[a][2])
		
		'''for a in range(self.neuronas_totales-len(self.se_quiere[0][:2])):
									print 'Umbral {} capa {} = {} '.format(self.umbrales[a][1],self.umbrales[a][0]+1,self.umbrales[a][2])'''
	
		print '\n'
		#print self.total2


		self.conexion_para_cada_neurona = []

		for a in range(len(self.total2)):
			self.conexion_para_cada_neurona+= [[self.total2[a][1],self.total2[a][2],self.total2[a][3]]]
		print self.conexion_para_cada_neurona
		
		'''wc = []
								for a in range(self.capas-1):#[[],[],[]]
									print a, 'asdaasdasdasdsaaaaaaaaaaaaaa'
									for i in range(len(total2)):
										if total2[a][1] is a:
											wc+=[[total2[i][4]],a]
									print wc, 'a ver si funciona we'''


		w = []
		c1=0
		d=0
		t=0
		for i in range(capas):
			d+=1
			for j in range(self.total_capas_neuronas[i][1]):
				c1+=1
				
				for k in range(len(self.total2)):
					t+=1
					w +=[self.conexion_para_cada_neurona[k][:]]
					#if w[k][1]
			self.perceptron+=[['capa '+str(i),'n_neurona '+str(j+1),'N_umbrales ' +str(self.umbrales[j][1]) if c1>2 else 'no hay',self.umbrales[c1-3][2] if c1>2 else 'no hay',['entradas recibidas' if c1>2 else 'datos']]]#,self.total_capas_neuronas[0][1],self.umbrales[0][0],self.umbrales[0][2],self.pesos_totales[0][2]]]
		
		


		#for a in range(self.neuronas_totales-1):
		#	self.perceptron+=[]



					#print b,a, 'para capa {}'.format(i+1)
		#print '\n',self.perceptron, '\ncapa, neurona, numero de umbral, valo de umbral'

		
	def calculaSalida(self):

		print self.total2[0][0][0]
		suma = []
		c = 0
		for a in range(1,self.capas):
			for j in range(self.total_capas_neuronas[a-1][1]):
				for i in range(self.total_capas_neuronas[a][1]):
					c+=1
					print a,j,i
					print suma
					suma+=[self.salidas[a-1][j]*self.total2[a-1][j][i][2]]
				#entradas_capas_ocultas+=[self.se_quiere[]]#cada numero de entrada [0,1],[1,1][1,0][0,0]*el peso que se conecta a la primera neurona. Asi sucesivbamente hasta que se alcance el numero total de neuronas en la primera capa oculta. Luego se anade ese dato al self.perceptron()






		'''#
								salida = 0
								total_de_pesos_por_capa = []
								c=0
								for a in range(self.capas):
									c+=1
									total_de_pesos_por_capa += [self.total_capas_neuronas[-1][1] if a>=2 else self.total_capas_neuronas[a+1][1]]
									print total_de_pesos_por_capa
								#salidaprimeras capas
						
								salida_primeras_capas = []
								for a in range(self.n_entradas):
									for i in range(self.total_capas_neuronas[0][1]):
										for k in range(total_de_pesos_por_capa[0]):
											salida_primeras_capas+=[self.conexion_para_cada_neurona[k][2]*self.se_quiere[a][i], '**{} hasta {} con entrada {}**'.format(i,k,a)]
								print salida_primeras_capas
											
														
								datos = []
								for i in range(len(self.se_quiere)):
									datos.append(self.se_quiere[i][:2])
								print 'entradas = ',datos'''


			#entrada21d = self.se_quiere[i][0]*self.pesos_totales[0]+self.se_quiere[i][1]*self.pesos_totales[2]+self.umbrales[0][2]
		#print A21


if __name__ == '__main__':
	Perceptron()