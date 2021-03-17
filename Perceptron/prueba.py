from __future__ import print_function
import math,random,time,os,sys,colorama,subprocess

import matplotlib.pyplot as plt


class Perceptron():
    def __init__(self):

        #Nota perceptron solo desde la capa oculta hasta la salida. Las capas de entradsa referenciar solo como variables los datos: En este caso es 1 y 0 
        self.capas = 4
        self.neuronas_por_capa = [2,4,4,1]
        self.entradas = []
        self.pesos = []
        self.umbrales = []#[[numero,valor]]#cada sub array es una ca
        #[[0,0,random]] [[[],[]]]
        self.tasaAprende = 0.01
        self.build()   
        
        #Para poder dibujuar
        self.x = []
        self.y = []     
        self.t = []
        
        self.xor = [[0,0],[1,0],[0,1],[1,1]]
        sale = [[0],[1],[1],[0]]
        conjuntoentradas = 4
        a=0
        error_total = []
        while True:
            if a%10000==0:
                print ('--------- Iteracion {} ---------'.format(a))
            for i in range(conjuntoentradas):
                self.entradas = [self.xor[i]]
                self.calculaSalida()
                self.backpropagation(sale[i],self.xor[i])
                error = abs(sale[i][0]-self.entradas[-1][0])


                if a%100000 ==0:

                    print (self.entradas[-1][0],'<vs>',sale[i],'  ',colorama.Fore.GREEN+'['+colorama.Fore.YELLOW+'+'+colorama.Fore.GREEN+']'+colorama.Fore.LIGHTBLUE_EX+' Error: '+colorama.Fore.LIGHTMAGENTA_EX,abs(sale[i][0]-self.entradas[-1][0]), colorama.Fore.LIGHTRED_EX,a,colorama.Fore.WHITE+'')
            
            if a%10000 ==0:
                self.actualizar_datos(sale[i][0],self.entradas[-1][0],self.xor[i])


            if error<0.01 :
                break
            a+=1
            if a>100000:
                self.__init__()


            #print (self.pesos)
        self.dibujo(conjuntoentradas)

        self.datos()
        self.demostrar()

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
                        self.pesos[a][j]+=[[a,j,i,random.randrange(0,1)]]#self.popopeso[c-1]]]

            #Umbrales
            self.u = 0
            for a in range(1,self.capas):
                for j in range(self.neuronas_por_capa[a]):
                    self.umbrales+=[[]]
            for i in range(1,self.capas):
                for j in  range(self.neuronas_por_capa[i]):
                    self.u+=1
                    self.umbrales[i]+=[[j,random.randrange(0,1)]]#self.popoumbral[u-1]]]
            self.umbrales=self.umbrales[1:-2]
            self.umbrales = [ele for ele in self.umbrales if ele !=[]]
            self.pesos = [el for el in self.pesos if el !=[]]
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
                self.pesos[1][j][k][3] = abs(self.pesos[1][j][k][3]-(self.tasaAprende*derror2))
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
                self.pesos[0][j][k][3] = abs(self.pesos[0][j][k][3]-self.tasaAprende*derror1)
        
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
                acum+=self.pesos[2][k][i][-1]*yi*(1-yi)*(-se[i]+yi)
            derror3 = self.entradas[2][k]*(1-self.entradas[2][k])*acum
            self.umbrales[1][k][1] = self.umbrales[1][k][1]-self.tasaAprende*derror3


        #Umbrales capa 2
        for k in range(self.neuronas_por_capa[1]):
            acumular = 0
            for p in range(self.neuronas_por_capa[2]):
                acum = 0
                for i in range(self.neuronas_por_capa[3]):
                    acum+=self.pesos[2][p][i][3]*yi*(1-yi)*(-se[i]+yi)
            derror2 = self.entradas[1][k]*(1-self.entradas[1][k])*acum
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
        centradas = input('Conjunto de entradas: ')
        try:int(centradas)
        except Exception as e:print (colorama.Fore.LIGHTYELLOW_EX+'Wachin, tenes que poner un numero bo\n\n'+e)

    
        for a in range(int(centradas)):
            self.entradas = []
            c = []

            for b in range(self.neuronas_por_capa[0]):
                n_entrada = input('Entrada '+str(b)+': ')
                c.append(int(n_entrada))
            self.entradas = [c]
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
        return self.entradas[-1][0]
    
    def actualizar_datos(self,x,y,t):

        self.x+=[x]
        self.y+=[y]
        self.t +=[t]

    
    def dibujo(self,c):
        #print (self.x,self.y)
   
        for i in range(len(self.x)):
            plt.plot(self.x[i],self.y[i],marker = 'o',color = 'red',label = 'Conjunto '+str(self.t[i]) )

        
        plt.title('Perceptron')
        plt.xlabel('Entrada')
        plt.ylabel('Salida')            
        plt.legend()
        plt.show()


if __name__=='__main__':
    Perceptron()
