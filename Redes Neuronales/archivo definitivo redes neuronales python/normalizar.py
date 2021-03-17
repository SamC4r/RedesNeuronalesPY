fx = 0
import multilayer as ml
class Norm():

    def __init__(self):
        self.calc()
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
        self.x_norm = []
        self.y_norm = []
        for i in range(len(self.x)):
            self.x_norm += [[self.formula(self.x,i)]]
            self.y_norm += [[self.formula(self.y,i)]]

        #print (self.x_norm,self.y_norm)
        ml.Perceptron.xor = self.x_norm
        ml.Perceptron.sale = self.y_norm



    def formula(self,lista, original):
        n=0
        n = (lista[original]-min(lista))/(max(lista)-min(lista))
        return n

if __name__  =='__main__':
    Norm()