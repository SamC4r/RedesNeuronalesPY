import random,math

class Perceptron():
	def __init__(self):
		self.pesos = []
		self.umbral = 0
		self.total_entradas = 2
		self.total_Neuronas = 5


		for a in range(self.total_entradas):
			self.pesos+=[a]
		

		

		self.entradas = [1,0]
		self.salidas = []
		for a in range(self.total_Neuronas):
			self.salidas+=[a]
		print self.salidas
		self.neuronas = []
		
		self.build()
		self.calculaSalida()
		self.calculaCapa()


	def build(self):
		

		#Crea capas
		for genera in range(self.total_Neuronas+1):
			self.neuronas+=[random.random(),genera]

		#print self.neuronas, 'genera'


		#Valores de pesos para capa 1
		for cont in range(self.total_entradas):
			self.pesos[cont]+=random.random()
		self.umbral = random.random()
		print self.pesos, self.umbral

		
	def calculaSalida(self):
		valor = 0
		a=[]
		for cont in range(self.total_entradas):
			print self.entradas[cont]
			valor += self.entradas[cont]*self.pesos[cont]
		valor+=self.umbral
		return 1/(1/math.exp(-valor))

	def calculaCapa(self):
		for cont in range(len(self.neuronas)):
			self.salidas[cont]= self.neuronas[cont].calculaSalida()


'''			salida = 0
			for cont in range(len(self.neuronas)):
				for i in range(self.total_entradas):
					salida+=self.entradas[i]*self.pesos[i]
					print salida
				self.salidas+=[salida]
			print self.salidas'''
		
if __name__=='__main__':
	Perceptron()