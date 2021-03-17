import matplotlib.pyplot as plt
import random

def basic_plot():
    x = [1,2,3]
    x2 =[4,5,6]
    y2 = [4,5,6]
    plt.plot(x,[1,2,3])

    plt.plot([1,2,3],[1,2,3], label = 'Second line')
    plt.plot(x2,y2,label = 'First Line')
    
    plt.xlabel('X')#X label
    plt.ylabel('Y')# y label
    
    plt.title('Yesssssssssssssss\nCheck it out')#titulo
    
    plt.legend()

    plt.show()#Para poder ver la window

#basic_plot()


def barcharts():
    x = [2,4,6,8,10]
    y = [6,7,3,2,4]

    x2 = [1,3,5,7,9]
    y2 = [2,1,7,4,8]

    plt.bar(x,y,label = 'bar 1',color = 'blue')
    plt.bar(x2,y2,label = 'bar 2',color = '#FF00C4')

    plt.title('hermano')
    plt.legend()#Activar los titulos de las barras
    plt.show()
    #Bar cuenta los datos tal cuales. para cada id hay una edad 

def histogram():
    pop = [65,4,22,55,78,12,45,85,16,34,95,39,44,23,31,98,100,27,83,83,18,19,20,21,29,39,47]
    ids = [x for x in range(len(pop))]
    #print (ids)
    plt.xlabel('N Persona')
    plt.ylabel('edad')
    #plt.bar(ids,pop,label = 'poblacion')
    bins = [x for x in range(120) if x%10==0] #--> [10,20,30,40]
    print (bins)
    plt.hist(pop,bins,histtype='bar',rwidth=.9)

    plt.legend()
    plt.show()
    #Histogram dice cuantas veces se repite dentro e ese intervalo de 10
    #para cada intervalo puede haber distintas personas. Cuenta las poersonas que stan en un intervalo de 10

#histogram()
#barcharts()


def scatterplot():#Diagrama de disperson
    
    x = [1,2,3,4,5,6,7,8,9]
    y= [5,2,5,7,1,3,7,9,0]


    plt.scatter(x,y,label = 'skitscat',color = '#00F5FF',marker = 'h',s = 200)
    
    
    
    plt.xlabel('X')#X label
    plt.ylabel('Y')# y label
    plt.title('Yesssssssssssssss\nCheck it out')#titulo
    plt.legend()
    plt.show()

#scatterplot()



def stack_plots():
    
    days = [1,2,3,4,5]
    sleeping = [7,8,6,11,7]
    eating =   [2,3,4,3,2]
    working =  [7,8,7,2,2]
    playing =  [8,5,7,8,13]

    plt.stackplot(days,sleeping,eating,working,playing,colors = ['m','k','g','b','r'])
    plt.plot([],[],color = 'm',label = 'sleeping',linewidth = 5)#Para poner leyena a los colores
    #No tienen labels los colores


    plt.xlabel('X')#X label
    plt.ylabel('Y')# y label
    plt.title('Yesssssssssssssss\nCheck it out')#titulo
    plt.legend()
    plt.show()
stack_plots()
