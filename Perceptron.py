import numpy as np
import random
from matplotlib import pyplot

class Perceptron:

    def __init__(self):

        self.w0 = 0.0
        self.w1 = 0.0
        self.w2 = 0.0
        self.bias = 0.0
        self.x0 = 0.0
        self.x1 = 0.0
        self.x2 = 0.0
        self.y = 0.0

        #* Listas creadas para guardar los puntos correspondientes del test
        self.puntosX = []
        self.puntosY = []
        self.puntosZ = []
        #* Lista para clasificar los puntos por colores y graficarlos
        self.clasifColores = []
        
        #*Listas para tener el set de prueba y entrenamiento de cada particion
        self.trainSet = []
        self.testSet = []

        #*Lista con el dataset
        self.dataset = []

    #*Metodo para crear una particion
    def makePartition(self):

        #*Toma la longitud de lineas del archivo del dataset para saber como dividir
        #*Los datos en 80% y 20%
        dataSetSize = len(self.dataset)
        trainPercent = int(dataSetSize*0.80)
        testPercent = int(dataSetSize*0.20)

        #*Con la libreria random se revuelven todas las lineas para tener los datos al azar
        random.shuffle(self.dataset)

        #*Se guardan los sets de train y test
        #*El 80%...
        self.trainSet = self.dataset[:trainPercent]
        #*El 20%
        self.testSet = self.dataset[trainPercent:dataSetSize]


    #*Funcion de activacion
    def funcActivacion(self, out):
        #*Se realiza la prediccion de acuerdo al valor obtenido de la sumatoria
        if out>=0:
            return 1
        return -1
    
    def sumatoria(self):

        return (self.x0*self.w0) + (self.x1*self.w1) + (self.x2*self.w2) +self.bias
    
    def ajustaPesos(self,factorAprendizaje, error):

        #*Cuando no se cumple con la prediccion y el error fue diferente a 0
        #* se hace el ajuste de los pesos y el bias
        self.setBias(factorAprendizaje*error)
        self.setW0(factorAprendizaje * error * self.x0)
        self.setW1(factorAprendizaje * error * self.x1)
        self.setW2(factorAprendizaje * error * self.x2)

    #*Funcion que servirá para el entrenamiento, usando el trainSet
    def trainPerceptron(self, factorAprendizaje=0.4,maxEpocas=500):

        row = []
        error = 0

        for epoca in range(maxEpocas):

            error = 0
            #! Si obtiene un valor distinto al esperado, sale del loop y comienza de nuevo
            for i in range(len(self.trainSet)):

                #* Coloca las entradas, en este ejercicio son 3, en coordenadas serian x,y y z
                row = self.trainSet[i]
                self.setX0(float(row[0]))
                self.setX1(float(row[1]))
                self.setX2(float(row[2]))
                self.setY(float(row[3]))
                #*Obtiene el valor Y
                sum = (self.sumatoria())

                #*Calcula el error (valor deseado - Y)
                error = self.getY() - (self.funcActivacion(sum))

                #! Si el error es diferente de 0, se ajustan los pesos y comienza de nuevo
                if error != 0:
                    self.ajustaPesos(factorAprendizaje, error)
                    break

    def testPerceptron(self, factorAprendizaje=0.4):

        row = []
        error = 0

        for i in range(len(self.testSet)):

            #* Coloca las entradas
            row = self.testSet[i]
            self.setX0(float(row[0]))
            self.setX1(float(row[1]))
            self.setX2(float(row[2]))
            self.setY(float(row[3]))
            #*Obtiene el valor Y
            sum = (self.sumatoria())

            #* Guarda en el array de colores la clasificacion que realiza el perceptron
            #! Si es igual a la salida deseada, se guarda verde, de lo contrario es rojo
            #! Lo que guarda es si esa linea del conjunto de datos fue predicha bien o mal
            if self.funcActivacion(sum) == self.getY():
                self.clasifColores.append('green')
            else:
                self.clasifColores.append('red')
            #*Calcula el error (valor deseado - Y)
            error = self.getY() - (self.funcActivacion(sum))

            #*Como es el metodo para testear, no se hace el ajuste de pesos

        #*Al final se grafican los puntos (c= colores de cada punto)
        self.crearPuntos()

        #pyplot.scatter(self.puntosX, self.puntosY, self.puntosZ, c=self.clasifColores)
        #pyplot.show()
        #print(f"Long X: {len(self.puntosX)} Long Y: {len(self.puntosY)} Long Color: {len(self.clasifColores)}")

    #*Metodo para trabajar con una particion, se hace el train y el test
    #*Recibe el dataset con el que se va a trabajar
    def startPartition(self, d):
        self.setDataset(d)
        #*Se crean los pesos y el bias
        self.setW0(np.random.rand())
        self.setW1(np.random.rand())
        self.setW2(np.random.rand())
        self.setBias(np.random.rand())

        #*Se inicia el entrenamiento
        self.trainPerceptron()
        #*Se hace el test
        self.testPerceptron()

    #*Metodo para crear las coordenadas de cada punto
    def crearPuntos(self):

        #*En este caso, solo interesa saber como es que predice los datos de test
        for i in range(len(self.testSet)):
            self.puntosX.append(float(self.testSet[i][0]))
            self.puntosY.append(float(self.testSet[i][1]))
            self.puntosZ.append(float(self.testSet[i][2]))

    #* Getters y setters
    def setW0(self,w):
        self.w0 = w

    def getW0(self):
        return self.w0
    
    def setW1(self,w):
        self.w1 = w

    def getW1(self):
        return self.w1
    
    def setW2(self, w):
        self.w2 = w

    def getW2(self):
        return self.w2
        
    def setBias(self, b):
        self.bias = b

    def getBias(self):
        return self.bias

    def setX0(self, x):
        self.x0 = x
    
    def getX0(self):
        return self.x0
    
    def setX1(self, x):
        self.x1 = x

    def getX1(self):
        return self.x1
    
    def setX2(self, x):
        self.x2 = x

    def getX2(self):
        return self.x2
    
    def setY(self, v):
        self.y = v

    def getY(self):
        return self.y
    
    def setDataset(self, d):
        self.dataset = d

    def getDataset(self):
        return self.dataset