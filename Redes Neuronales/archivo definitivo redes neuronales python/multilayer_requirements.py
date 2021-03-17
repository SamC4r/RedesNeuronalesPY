import time,os,sys,subprocess


class Requirements():
    def __init__(self):

        subprocess.run('python3 -m pip install --upgrade pip')

        instalando = True
        txt = '***\n'
        for dm in 'Instalando paquetes':
            sys.stdout.write(dm)
            sys.stdout.flush()
            time.sleep(0.062)
        time.sleep(2)
        
        for a in txt:
            sys.stdout.write(a)
            sys.stdout.flush()
            time.sleep(0.062)
                
        self.instalar()
        self.multilayer_ex()

          
    def instalar(self):
        for i in 'Instalando Colorama... ':
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(0.08)
        try:
            subprocess.run('pip3 install --upgrade colorama')
        except Exception as e: print ("Error\n "+e)
        for i in 'Instalando Matplotlib... ':
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(0.08)
        try:
            subprocess.run('pip3 install --upgrade matplotlib')
            subprocess.run('pip3 install --upgrade numba')
            instalando = False
        except Exception as e: print ("Error de pip\n "+e)

    def multilayer_ex(self):
        for i in 'Ejecutando Multilayer...\n\n\n':
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(0.08)
        time.sleep(1)
        ml.Perceptron()




if __name__ == '__main__':

    try:
        import multilayer_xor as ml
        Requirements()
    except Exception as e: 
        
        print ('sad')            
    
        print ('\n\n\n＼（〇_ｏ）／ Tenes que tener el archivo de multilayer en el mismo archivo que este\nGuevon Equis de\nO... El pip no te funciona. intenta copn otra version de pytohn (Ejecutalo en python3). xd\n\n',e)


    