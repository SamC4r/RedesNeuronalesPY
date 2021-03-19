from __future__ import print_function
import math,random,time,os,sys,colorama,subprocess

import matplotlib.pyplot as plt
import normalizar as nm


class Perceptron():
    def __init__(self):

        #Nota: perceptron solo desde la capa oculta hasta la salida. Las capas de entradsa referenciar solo como variables los datos: En este caso es 1 y 0 
        self.capas = 4
        self.neuronas_por_capa = [1,4,4,1]
        self.entradas = []
        self.pesos = []
        self.umbrales = []#[[numero,valor]]#cada sub array es una ca
        #[[0,0,random]] [[[],[]]]
        self.tasaAprende = 0.4
        self.build()   
        self.calc()
        #Para poder dibujuar
           
        
        
        
        print (self.xor, '\n\n\n\n',self.sale)
        #time.sleep(20)
            #print (self.pesos)ss

        conjuntoentradas = 40

        for a in range(1,4002):
            if a%2000==0:
                print ("\n------ Iteracion {} ------".format(a))            
            for i in range(conjuntoentradas):
                
                self.entradas = [self.xor[i]]
                self.calculaSalida()
                self.backpropagation(self.sale[i],self.xor[i])

                if a%2000 == 0:
                    print (self.entradas[-1][0],'<vs>',self.sale[i],'  ',colorama.Fore.GREEN+'['+colorama.Fore.YELLOW+'+'+colorama.Fore.GREEN+']'+colorama.Fore.LIGHTBLUE_EX+' Error: '+colorama.Fore.LIGHTMAGENTA_EX,abs(self.sale[i][0]-self.entradas[-1][0]), colorama.Fore.LIGHTRED_EX,a,colorama.Fore.WHITE+'')
                if a%1000==0:
                    self.actualizar_datos(self.xor[i][0],self.sale[i][0])
        self.dibujo(conjuntoentradas)

        self.datos()
        self.demostrar()


    def calc(self):
        i= -2
        self.x = []
        self.y = []

        for a in range(40):
            i+=0.1
            self.y += [i**3-i]
            self.x +=[i]
            #print ('x: {}   y: {}'.format(x,y))
        self.normalizar()

    def normalizar(self):
        self.xor = []
        self.sale = []
        for i in range(len(self.x)):
            self.xor+= [[self.formula(self.x,i)]]
            self.sale += [[self.formula(self.y,i)]]

        print (self.xor,self.sale)
        time.sleep(10)



    def formula(self,lista, original):
        n=0
        n = (lista[original]-min(lista))/(max(lista)-min(lista))
        return n
        
    def build(self):
       # pesos_ordenados_segun_siguiente_neurona = [] #[[todos lospesos que llegan a neurona 1 capa 2,todos lospesos que llegan a neurona 2 capa 2 ]]
        #PESOS
        const = False
        while not const:
            self.c = 0
        
            for a in range(self.capas-1):
                for j in range(self.neuronas_por_capa[a]):
                    self.pesos+=[[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]]
                    
            for a in range(self.capas-1):
                if a >=self.capas:break
                for j in range(self.neuronas_por_capa[a]):
                    for i in range(self.neuronas_por_capa[a+1]):
                        self.c+=1
                        self.pesos[a][j]+=[[a,j,i,random.random()]]#self.popopeso[c-1]]]

            #Umbrales
            self.u = 0
            for a in range(1,self.capas):
                for j in range(self.neuronas_por_capa[a]):
                    self.umbrales+=[[]]
            for i in range(1,self.capas):
                for j in  range(self.neuronas_por_capa[i]):
                    self.u+=1
                    self.umbrales[i]+=[[j,random.random()]]#self.popoumbral[u-1]]]
            self.umbrales=self.umbrales[1:-2]
            self.umbrales = [ele for ele in self.umbrales if ele !=[]]
            self.pesos = [el for el in self.pesos if el !=[]]
            #print (self.pesos, 'PEsos')
            const = True
    def calculaSalida(self):
        #suma = 0

        for a in  range(self.capas):
            self.entradas+=[[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]]
        #print lista_suma
        for a in range(1,self.capas):

            for i in range(self.neuronas_por_capa[a]):       
                self.entradas[a][i] = 0
                for j in range(self.neuronas_por_capa[a-1]):

                    #print self.entradas[a-1][j],self.pesos[a-1][j][i][3]
                    #print self.entradas[a-1][j],self.pesos[a-1][j][i][3]
                    self.entradas[a][i] += self.entradas[a-1][j]*self.pesos[a-1][j][i][3]
                                    
                self.entradas[a][i]+=self.umbrales[a-1][i][1]

                self.entradas[a][i] = (1)/(1+(math.exp(-self.entradas[a][i])))
        
        self.entradas = self.entradas[:4]
       # print self.entradas


    def backpropagation(self,se,e):
        ###PARA PESOS###
        #Procesa capa 4
        #variacion del error con respecto a los pesos de la capa 3
        
        
        for j in range(self.neuronas_por_capa[2]):
            for i in range(self.neuronas_por_capa[3]):
                yi = self.entradas[3][i]
                derror = self.entradas[2][j]*yi*(1-yi)*(-se[i]+yi)
                #print 'error', derror3
                self.pesos[2][j][i][3] = self.pesos[2][j][i][3]-(self.tasaAprende*derror)
        
        #Procesa capa 3
        for j in range(self.neuronas_por_capa[1]):
            for k in range(self.neuronas_por_capa[2]):
                acum = 0
                for i in range(self.neuronas_por_capa[3]):
                    yi = self.entradas[3][i]
                    acum+=self.pesos[2][k][i][3]*yi*(1-yi)*(-se[i]+yi)
                derror2  = self.entradas[1][j]*self.entradas[2][k]*(1-self.entradas[2][k])*acum
                self.pesos[1][j][k][3] = self.pesos[1][j][k][3]-(self.tasaAprende*derror2)
        #Procesa capa 2
        
        for j in range(self.neuronas_por_capa[0]):
            for k in  range(self.neuronas_por_capa[1]):
                acumular = 0
                for p in range(self.neuronas_por_capa[2]):
                    acum = 0
                    for i in range(self.neuronas_por_capa[-1]):
                        yi = self.entradas[3][i]
                        acum+= self.pesos[2][p][i][3]*yi*(1-yi)*(-se[i]+yi)
                    acumular+=self.pesos[1][k][p][3]*self.entradas[2][p]*(1-self.entradas[2][p])*acum
                derror1 = e[j] * self.entradas[1][k] * (1-self.entradas[1][k]) * acumular
                self.pesos[0][j][k][3] = self.pesos[0][j][k][3]-self.tasaAprende*derror1
        
        ###Para UMBRALES###
        #Umbrales capa 4
        for i in range(self.neuronas_por_capa[3]):
            yi = self.entradas[3][i]
            derror4 = yi*(1-yi)*(-se[i]+yi)
            self.umbrales[2][i][1] = self.umbrales[2][i][1]-self.tasaAprende*derror4

                #Umbrales capa 3

        for k in range(self.neuronas_por_capa[2]):
            acum = 0
            for i in range(self.neuronas_por_capa[3]):
                yi = self.entradas[3][i]
                acum+=self.pesos[2][k][i][3]*yi*(1-yi)*(-se[i]+yi)
            derror3 = self.entradas[2][k]*(1-self.entradas[2][k])*acum
            self.umbrales[1][k][1] = self.umbrales[1][k][1]-self.tasaAprende*derror3


        #Umbrales capa 2
        for k in range(self.neuronas_por_capa[1]):
            acumular = 0
            for p in range(self.neuronas_por_capa[2]):
                acum = 0
                for i in range(self.neuronas_por_capa[3]):
                    acum+=self.pesos[2][p][i][3]*yi*(1-yi)*(-se[i]+yi)
                acumular+=self.pesos[1][k][p][3]*self.entradas[2][p]*(1-self.entradas[2][p])*acum
            derror2 = self.entradas[1][k]*(1-self.entradas[1][k])*acumular
            self.umbrales[0][k][1] = self.umbrales[0][k][1]-self.tasaAprende*derror2
            #print self.umbrales[0][k][1], 'U(1)'

    def datos(self):
        fin = '\n\n'+colorama.Fore.LIGHTYELLOW_EX+'***'+colorama.Fore.LIGHTGREEN_EX+'Entrenamiento completado'+colorama.Fore.LIGHTYELLOW_EX+'***'
        folder = os.path.dirname(os.path.abspath(__file__))
        file1 = os.path.join(folder,'entrenamiento.txt')
        umbrales = '\n\nTotal Umbrales: {} --> {} \n'.format(self.u,self.umbrales)
        pesos = '\n\nTotal Pesos: {} --> {}\n '.format(self.c,self.pesos)
        for a in fin:
            sys.stdout.write(a)
            sys.stdout.flush()
            time.sleep(0.062)

        time.sleep(1)
        print (colorama.Fore.LIGHTBLUE_EX+'\ndatos guardados en',os.getcwd(),'/entrenamiento.txt')
        file1 = open('entrenamiento.txt','w')
        file1.write(umbrales)
        file1.write(pesos)
        file1.close()

        

    def demostrar(self):
        print ('\n')
        for dm in colorama.Fore.RED+'Demostracion':
            sys.stdout.write(dm)
            sys.stdout.flush()
            time.sleep(0.062)
        print (colorama.Fore.WHITE +'\n')
        q = input('Volver a entrenar (Y/n): ')
        if q == 'Y' or q == 'y' or q == 'yes':self.__init__()

        centradas = input('Conjunto de entradas: ')
        try:int(centradas)
        except Exception as e:print (colorama.Fore.LIGHTYELLOW_EX,'Wachin, tenes que poner un numero bo\n\n',e)

    
        for a in range(int(centradas)):
            self.entradas = []
            c = []

            for b in range(self.neuronas_por_capa[0]):
                n_entrada = input('Entrada '+str(b)+': ')
                c.append(float(n_entrada))
            self.entradas += [c]
            print (self.salida_nueva())
            
          
        


    def salida_nueva(self):
        for a in  range(self.capas):
            self.entradas+=[[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]]
        for a in range(1,self.capas):
   
            for i in range(self.neuronas_por_capa[a]):       
                self.entradas[a][i] = 0
                for j in range(self.neuronas_por_capa[a-1]):

                    #print self.entradas[a-1][j],self.pesos[a-1][j][i][3]
                    #print self.entradas[a-1][j],self.pesos[a-1][j][i][3]
                    self.entradas[a][i] += self.entradas[a-1][j]*self.pesos[a-1][j][i][3]
                                    
                self.entradas[a][i]=self.entradas[a][i]+self.umbrales[a-1][i][1]

                self.entradas[a][i] = (1)/(1+(math.exp(-self.entradas[a][i])))
        
        self.entradas = self.entradas[:4]       
        return self.entradas[-1]
    
    def actualizar_datos(self,x,y):

        self.x+=[x]
        self.y+=[y]

    
    def dibujo(self,c):
        #print (self.x,self.y)
   
        
        plt.plot(self.x,self.y,marker = 'o',color = 'red')
        
        plt.plot(self.xor,self.sale,color = 'blue', label = 'Original')
        plt.title('Perceptron')
        plt.xlabel('Entrada')
        plt.ylabel('Salida')    
        plt.legend()        
        plt.show()


if __name__=='__main__':
    Perceptron()
