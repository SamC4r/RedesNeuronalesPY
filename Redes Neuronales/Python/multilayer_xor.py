from __future__ import print_function
import math,random
import time
import os,sys, subprocess
import colorama
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.pyplot import show
from numba import jit
import keyboard


'''
© Creado por Samuel Caraballo Chichiraldi (16 y/o) 19 Marzo 2021 Ultima actualizacion © Xd

Red Neuronal con backpropagation en python sin numpy

-------------------------------------------------------------------------------------
Las redes de neuronas artificiales son una herramienta atractiva para solucionar problemas
de clasificación como el reconocimiento de caracteres manuscritos, el reconocimiento de
palabras habladas, y el diagnóstico de diferentes enfermedades.
Entre las más utilizadas se encuentra el algoritmo de retropropagación debido a la naturaleza
de su proceso de aprendizaje, que solamente necesita de dos ecuaciones para propagar las
señales de error hacia atrás, para obtener esas ecuaciones se utilizaran tres técnicas
importantes en matemáticas que es la función de error, gradiente descendiente y la regla de
la cadena

En resumen, Cajas negras con controles analogicos capaces de modificar una salida.
-------------------------------------------------------------------------------------

youtube: https://www.youtube.com/channel/UCeW0S9_GBxk4jLFAlafStsw
'''


#Se define la clase en donde pasa la magia
class Perceptron():
    def __init__(self):

        #Nota: perceptron solo desde la capa oculta hasta la salida. Las capas de entradsa referenciar solo como variables. los datos: caso de XOR es 1 y 0.
        # #Es decir solo la capa oculta realizaoperaciones 
        self.capas = 4 #Numero de capas
        self.neuronas_por_capa = [1,4,4,1] #neuronas definidas por capas
        self.entradas = [] #Array con cada salida de cada neurona del perceptron  [[1,0],[[.08912,.019238],[0.9871237]]] el subarray indica la capa y el otro la neurona
        self.pesos = [] #Pesos definidos en un array 4d [capa,[numero de neurona,[numero de peso con sus valores (j,i,random.random())]]]
        self.umbrales = []#[[numero,valor]]#cada sub array es una ca
        #[[0,0,random]] [[[],[]]]
        self.tasaAprende = 0.4 
        self.build()   #Se ejecuta el metodo que calcula todos los pesos y umbrales, les asigna un valor y determina su posicion en la red 
        
        #Para poder dibujuar
        self.x = []
        self.y = []

        #Entradas   funcion x^3-x normalizada  
        self.xor =[[0.0], [0.025641025641025654], [0.05128205128205131], [0.07692307692307697], [0.10256410256410262], [0.12820512820512828], [0.15384615384615394], [0.1794871794871796], [0.20512820512820523], [0.2307692307692309], [0.25641025641025655], [0.28205128205128216], [0.30769230769230776], [0.3333333333333334], [0.3589743589743591], [0.38461538461538464], [0.41025641025641024], [0.4358974358974359], [0.46153846153846156], [0.48717948717948717], [0.5128205128205128], [0.5384615384615384], [0.5641025641025641], [0.5897435897435898], [0.6153846153846154], [0.6410256410256411], [0.6666666666666666], [0.6923076923076923], [0.717948717948718], [0.7435897435897434], [0.7692307692307692], [0.7948717948717947], [0.8205128205128205], [0.846153846153846], [0.8717948717948718], [0.8974358974358974]]#, [0.9230769230769231], [0.9487179487179487], [0.9743589743589745], [1.0]]  #Ejemplo funcion x^3-x -->  #Ambos array tienen que ser 2d para que sea mas facil procesar el algoritmo de backpropagation
        #SAlidas esperadas
        self.sale =[[0.0], [0.09499041883383512], [0.1795784286887489], [0.2543115247741581], [0.31973720229947966], [0.37640295647413063], [0.4248562825075277], [0.46564467560908807], [0.4993156309882284], [0.5264166438543658], [0.5474952094169171], [0.5630988228852991], [0.573774979468929], [0.5800711743772234], [0.5825349028195996], [0.5817136600054742], [0.5781549411442642], [0.5724062414453867], [0.5650150561182582], [0.556528880372296], [0.5474952094169169], [0.5384615384615378], [0.5299753627155755], [0.5225841773884471], [0.5168354776895695], [0.5132767588283597], [0.5124555160142342], [0.5149192444566104], [0.521215439364905], [0.5318915959485349], [0.5474952094169171], [0.5685737749794684], [0.5956747878456059], [0.6293457432247463], [0.6701341363263067], [0.718587462359704]]#, [0.7752532165343551], [0.8406788940596768], [0.915411990145086], [1.0]]
        
        conjuntoentradas = len(self.xor)
        
        for a in range(50000):
            #!!!!!Importante!!!!!!!!:para cada iiteracion se envia cada conjunto al metodo calcula salida y se ajusta los pesos correspondientes
            if a%10000==0:
                print ("------ Iteracion {} ------".format(a))
            for i in range(conjuntoentradas):
                
                self.entradas = [self.xor[i]]#Se asigna el valor de la entraa externa al perceptron
                self.calculaSalida()#Calcula la salida con foward propagation
                self.backpropagation(self.sale[i],self.xor[i])#Ajusta Pesos y Umbrales con Backpropagation

                if a%10000 == 0:

                    print (self.entradas[-1][0],'<vs>',self.sale[i],'  ',colorama.Fore.GREEN+'['+colorama.Fore.YELLOW+'+'+colorama.Fore.GREEN+']'+colorama.Fore.LIGHTBLUE_EX+' Error: '+colorama.Fore.LIGHTMAGENTA_EX,abs(self.sale[i][0]-self.entradas[-1][0]), colorama.Fore.LIGHTRED_EX,a,colorama.Fore.WHITE+'')
                    #Evalua la variacion de los resultados cada 2000 iteraciones
                    
                    #Actualiza los datos para ver como se adapta la red a la funcion inicial. Importante si se utliza el ejemplo de la funcion normalizada
                if a%10000==0:     
                    self.actualizar_datos(self.xor[i][0],self.entradas[-1][0])
            if a%10000==0:     
                self.dibujo()

        #Grafica final
        self.datos()#Comienza con la demostracion de lo que se aprendio
        self.demostrar()#Utiliza los pesos ajustados para calcular foward propagation y obtener una salida. Importante para predecir

    def build(self):
        
        #PESOS. Me gusta poner a en vez de k :) como variable jeje
        self.c = 0 #variable que cuenta el numero de pesos
        
        for a in range(self.capas-1):
            for j in range(self.neuronas_por_capa[a]):
                self.pesos+=[[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]]
                #Para poder definir los pesos como se dijo en la linea 38
        
        for a in range(self.capas-1):
            if a >=self.capas:break
            for j in range(self.neuronas_por_capa[a]):
                for i in range(self.neuronas_por_capa[a+1]):
                    self.c+=1
                    self.pesos[a][j]+=[[a,j,i,random.random()]]#Asigna valores al azar

            #Umbrales
        self.u = 0 #variable que cuenta el numero de umbrales
        for a in range(1,self.capas):
            for j in range(self.neuronas_por_capa[a]):
                self.umbrales+=[[]]

        for i in range(1,self.capas):
            for j in  range(self.neuronas_por_capa[i]):
                self.u+=1
                self.umbrales[i]+=[[j,random.random()]]
        self.umbrales=self.umbrales[1:-2]#Remueve sublistas vacias
        self.umbrales = [ele for ele in self.umbrales if ele !=[]]#Remueve sublistas vacias
        self.pesos = [el for el in self.pesos if el !=[]]
        #print (self.pesos, 'PEsos')
            
    def calculaSalida(self):
        #utiliza foward propagation

        for a in  range(self.capas):
            self.entradas+=[[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]]
        for a in range(1,self.capas):

            for i in range(self.neuronas_por_capa[a]):       
                self.entradas[a][i] = 0

                for j in range(self.neuronas_por_capa[a-1]):

                    self.entradas[a][i] += self.entradas[a-1][j]*self.pesos[a-1][j][i][3]
                                    
                self.entradas[a][i]+=self.umbrales[a-1][i][1]

                self.entradas[a][i] = (1)/(1+(math.exp(-self.entradas[a][i])))#Sigmoide
        
        self.entradas = self.entradas[:4]#remueve algunas listas vacias


    def backpropagation(self,se,e):
        ###Todo basado en las formulas reales sin cambios significativos###


        ###PARA PESOS###
        
        #Procesa capa 4
        #variacion del error con respecto a los pesos de la capa 3
    
        for j in range(self.neuronas_por_capa[2]):
            for i in range(self.neuronas_por_capa[3]):
                yi = self.entradas[3][i]
                derror = self.entradas[2][j]*yi*(1-yi)*(-se[i]+yi)
                #print 'error', derror3
                self.pesos[2][j][i][3] = self.pesos[2][j][i][3]-(self.tasaAprende*derror)#modifica pesos. 
        
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
        print (umbrales,'\n\n\n',pesos,'\n\n\n')
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
        except Exception:print (colorama.Fore.LIGHTYELLOW_EX+'Wachin, tenes que poner un numero bo\n\n')

    
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


        self.x+=[x]#actualiza datos x
        self.y+=[y]#actualiza datos ys
    
    def dibujo(self):
        #print (self.x,self.y)
        style.use('fivethirtyeight')
        fig = plt.figure()
        ax1 = fig.add_subplot(1,1,1)
        ax1.clear()
        plt.plot(self.x,self.y,color = 'red',marker = '.')#funcion obtenida
        ax1.plot(self.xor,self.sale,color = 'blue',label = 'Original',marker = 'o')#funcion original
        plt.title('Perceptron')
        plt.xlabel('Entrada')
        plt.ylabel('Salida')    
        plt.show(block = True)

        self.x = []
        self.y = []



if __name__=='__main__':
    Perceptron()