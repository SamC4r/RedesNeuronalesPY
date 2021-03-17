from __future__ import print_function
import math,random,time,os,sys,colorama,subprocess

import matplotlib.pyplot as plt
from numba import jit


'''
© Creado por Samuel Caraballo Chichiraldi (16 y/o) 17 Marzo 2021 Ultima actualizacion ©

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
        
        self.xor =[[1,1],[1,0],[0,1],[0,0]] # Ejemplo de uncion normalizada x[[0.0], [0.025641025641025654], [0.05128205128205131], [0.07692307692307697], [0.10256410256410262], [0.12820512820512828], [0.15384615384615394], [0.1794871794871796], [0.20512820512820523], [0.23076923076923087], [0.2564102564102565], [0.2820512820512821], [0.30769230769230776], [0.3333333333333334], [0.35897435897435903], [0.3846153846153846], [0.41025641025641024], [0.4358974358974359], [0.4615384615384615], [0.48717948717948717], [0.5128205128205128], [0.5384615384615384], [0.5641025641025641], [0.5897435897435898], [0.6153846153846153], [0.641025641025641], [0.6666666666666666], [0.6923076923076923], [0.717948717948718], [0.7435897435897434], [0.7692307692307692], [0.7948717948717947], [0.8205128205128205], [0.846153846153846], [0.8717948717948718], [0.8974358974358974], [0.9230769230769231], [0.9487179487179487], [0.9743589743589745], [1.0]]
        self.sale = [[0],[1],[1],[0]]# Ejemplo de uncion normalizada y[[0.0], [0.08458800985491378], [0.15932110594032298], [0.22474678346564456], [0.2814125376402955], [0.32986586367369264], [0.37065425677525293], [0.4043252121543933], [0.4314262250205307], [0.45250479058308196], [0.46810840405146403], [0.47878456063509384], [0.48508075554338836], [0.4875444839857645], [0.4867232411716391], [0.4831645223104291], [0.47741582261155147], [0.47002463728442306], [0.46153846153846084], [0.4525047905830817], [0.44347111962770264], [0.4349849438817404], [0.427593758554612], [0.4218450588557344], [0.41828633999452447], [0.4174650971803991], [0.4199288256227753], [0.42622502053106986], [0.4369011771146997], [0.45250479058308196], [0.47358335614563324], [0.5006843690117707], [0.5343553243909113], [0.5751437174924716], [0.6235970435258689], [0.6802627977005199], [0.7456884752258417], [0.8204215713112509], [0.9050095811661649], [1.0]]
        #Ambos array tienen que ser 2d para que sea mas facil procesar el algoritmo de backpropagation
        
        conjuntoentradas = 2

        for a in range(18001):
            #!!!!!Importante!!!!!!!!:para cada iiteracion se envia cada conjunto al metodo calcula salida y se ajusta los pesos correspondientes
            if a%2000==0:
                print ("------ Iteracion {} ------".format(a))            
            for i in range(conjuntoentradas):
                
                self.entradas = [self.xor[i]]#Se asigna el valor de la entraa externa al perceptron
                self.calculaSalida()#Calcula la salida con foward propagation
                self.backpropagation(self.sale[i],self.xor[i])#Ajusta Pesos y Umbrales con Backpropagation

                if a%2000 == 0:
                    print (self.entradas[-1][0],'<vs>',self.sale[i],'  ',colorama.Fore.GREEN+'['+colorama.Fore.YELLOW+'+'+colorama.Fore.GREEN+']'+colorama.Fore.LIGHTBLUE_EX+' Error: '+colorama.Fore.LIGHTMAGENTA_EX,abs(sale[i][0]-self.entradas[-1][0]), colorama.Fore.LIGHTRED_EX,a,colorama.Fore.WHITE+'')
                    #Evalua la variacion de los resultados cada 2000 iteraciones
                if a==17999:#Actualiza los datos para ver como se adapta la red a la funcion inicial. Importante si se utliza el ejemplo de la funcion normalizada
                    self.actualizar_datos(self.xor[i][0],self.entradas[-1][0])
            #print (self.pesos)

        self.dibujo(conjuntoentradas)#Compara la grafica real con la obtenida 

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

        self.x+=[x]#actualiza datos x
        self.y+=[y]#actualiza datos ys

    
    def dibujo(self,c):
        #print (self.x,self.y)
   
        plt.plot(self.x,self.y,color = 'yellow',marker = '*')#funcion obtenida
        plt.plot(self.xor,self.s,color = 'blue',marker = 'o')#funcion original
        plt.title('Perceptron')
        plt.xlabel('Entrada')
        plt.ylabel('Salida')            
        plt.show()


if __name__=='__main__':
    jit()(Perceptron())#No c pero creo que aytuda a mejorar la rapidez del programa
