import random,math,os,time

class Perceptron():
	def __init__(self):
		self.tasaAprende = 0.6
		self.capas = 3
		self.neuronas_capa = [2,2,1]
		self.perceptron = []#[n_neuronas,[umbrales],[pesos],[salida de cada neurona de la capa]]
		self.cwd = os.getcwd()#current workin directory para guardar los datos en el cwd
		self.save = self.cwd + 'ResultadosPerceptron.txt'
		self.trainingdata = []
		self.build()
		#self.calculaSalida()
		self.train()

		#Printea los esultados paa cada entrada d ela neuorna
		while True:
			for i in range(self.perceptron[0][0]):
				#self.perceptron[0][3][i] = raw_input('entrada'+str(i)+' : ')
				print self.perceptron, 'asd'
			self.calculaSalida()

	def build(self):
		print '**Cargando Neurona***'
		time.sleep(2)
		for i in range(self.capas):
			capa = []
			u = []
			w = []
			a = []
			capa.append(self.neuronas_capa[i])#raw_input('neuronas capa '+str(i)+': ')))
			print capa, 'capa '+str(i)
			for j in range(capa[0]):
				u.append(random.random())
				a.append(random.random())
				wc = [] #Pesos 
				if i!=0:
					for k in range(self.perceptron[i-1][0]):
						wc.append(random.random())
						print k,'l'
				w.append(wc)
				capa.append(u)
				capa.append(w)
				capa.append(a)
				print capa,' capa'
				self.perceptron.append(capa)


	def calculaSalida(self):

		print 'salida de las neuronas capa 0'
		print self.perceptron[0][3], 'sdasd'
		for k in range(len(self.perceptron)-1):#paa k de la capa anterior
			for i in range(self.perceptron[k+1][0]):# para numero de neuronas de la capa actual
				suma = 0
				print self.perceptron[k][0],'pppppppppppppppppp'
				for j in range(self.perceptron[k][0]):
					print j
					

					suma =suma+(self.perceptron[k][3][j]*self.perceptron[k+1][2][i][0])
					print self.perceptron[k][3][j], self.perceptron[k][3][i][j] , 'asdasd'
				suma +=self.perceptron[k+1][1][i]
				suma = 1/(1+math.exp(-suma))
				self.perceptron[k+1][3][i]=suma
			print 'salida de las neuronas capa {} = {}'.format(k+1,self.perceptron[k+1][3])



	def train(self):
		pass
if __name__ =='__main__':
	Perceptron()