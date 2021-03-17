from __future__ import print_function
import math,random,time,os,sys,colorama,subprocess

import matplotlib.pyplot as plt
from numba import jit


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
        
        #Para poder dibujuar
        self.x = []
        self.y = []     
        
        self.xor = [[0.0], [0.025641025641025654], [0.05128205128205131], [0.07692307692307697], [0.10256410256410262], [0.12820512820512828], [0.15384615384615394], [0.1794871794871796], [0.20512820512820523], [0.23076923076923087], [0.2564102564102565], [0.2820512820512821], [0.30769230769230776], [0.3333333333333334], [0.35897435897435903], [0.3846153846153846], [0.41025641025641024], [0.4358974358974359], [0.4615384615384615], [0.48717948717948717], [0.5128205128205128], [0.5384615384615384], [0.5641025641025641], [0.5897435897435898], [0.6153846153846153], [0.641025641025641], [0.6666666666666666], [0.6923076923076923], [0.717948717948718], [0.7435897435897434], [0.7692307692307692], [0.7948717948717947], [0.8205128205128205], [0.846153846153846], [0.8717948717948718], [0.8974358974358974], [0.9230769230769231], [0.9487179487179487], [0.9743589743589745], [1.0]]
        sale = [[0.0], [0.08458800985491378], [0.15932110594032298], [0.22474678346564456], [0.2814125376402955], [0.32986586367369264], [0.37065425677525293], [0.4043252121543933], [0.4314262250205307], [0.45250479058308196], [0.46810840405146403], [0.47878456063509384], [0.48508075554338836], [0.4875444839857645], [0.4867232411716391], [0.4831645223104291], [0.47741582261155147], [0.47002463728442306], [0.46153846153846084], [0.4525047905830817], [0.44347111962770264], [0.4349849438817404], [0.427593758554612], [0.4218450588557344], [0.41828633999452447], [0.4174650971803991], [0.4199288256227753], [0.42622502053106986], [0.4369011771146997], [0.45250479058308196], [0.47358335614563324], [0.5006843690117707], [0.5343553243909113], [0.5751437174924716], [0.6235970435258689], [0.6802627977005199], [0.7456884752258417], [0.8204215713112509], [0.9050095811661649], [1.0]]
        self.s = sale
        conjuntoentradas = 40

        for a in range(6001):
            if a%2000==0:
                print ("------ Iteracion {} ------".format(a))            
            for i in range(conjuntoentradas):
                
                self.entradas = [self.xor[i]]
                self.calculaSalida()
                self.backpropagation(sale[i],self.xor[i])

                if a%2000 == 0:
                    

                    print (self.entradas[-1][0],'<vs>',sale[i],'  ',colorama.Fore.GREEN+'['+colorama.Fore.YELLOW+'+'+colorama.Fore.GREEN+']'+colorama.Fore.LIGHTBLUE_EX+' Error: '+colorama.Fore.LIGHTMAGENTA_EX,abs(sale[i][0]-self.entradas[-1][0]), colorama.Fore.LIGHTRED_EX,a,colorama.Fore.WHITE+'')
                if a==5999:
                    self.actualizar_datos(self.xor[i][0],self.entradas[-1][0])
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
                    self.pesos+=[[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]]
                    
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
        centradas = input('Conjunto de entradas: ')
        try:int(centradas)
        except Exception as e:print (colorama.Fore.LIGHTYELLOW_EX+'Wachin, tenes que poner un numero bo\n\n'+e)

    
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
        return self.entradas[-1][0]
    
    def actualizar_datos(self,x,y):

        self.x+=[x]
        self.y+=[y]

    
    def dibujo(self,c):
        #print (self.x,self.y)
   
        for i in range(len(self.x)):
            plt.plot(self.x[i],self.y[i],marker = 'o',color = 'red',)
        plt.plot(self.x,self.y,color = 'yellow',marker = '*')
        plt.plot(self.xor,self.s,color = 'blue',marker = 'o')
        plt.title('Perceptron')
        plt.xlabel('Entrada')
        plt.ylabel('Salida')            
        plt.show()


if __name__=='__main__':
    jit()(Perceptron())
