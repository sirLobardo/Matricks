# Matricks
# Coded By sirLobardo

#If you want to use this libraries, you need to install them
# type on terminal 
#pip install matplotlib numpy

#import matplotlib.pyplot as plt
#import math
#import numpy as np

#Prinumtest is a class that tests if a number is prime or not 
#and so returns the result in boolean variable by isPrime function

class Prinumtest:
    
    def __init__(self, numero):
       self.num = int(numero) 
    pass

    def isPrime(self):
        x = 0
        y = 0
        if self.num == 2: return True
        if self.num % 2 == 0 or self.num == 1 or self.num == - 1: return False
        else:
            for x in range(int(round(self.num / 2 ))):
                if self.num % (x + 1) == 0: y = 1 + y
                if y > 2: break
        if y > 2: return False
        else: return True
#Fibo is a class that receives a position of fibonnaci sequence
#and returns a list with the sequence by list function

class Fibo:
    def __init__(self, position):
       self.p = abs(int(position)) 
    pass

    def list(self):
        list = [1, 1]
        i = 2
        while i < self.p:
            list.insert(i, list[i - 2] + list[i - 1] )
            i = i + 1
        return list
        
    def aodd(self):
        list = Fibo(self.p).list()
        y = 0
        for x in range(self.p):
            if list[x] % 2 != 0: 
                y = y + 1
        return y

    def aeven(self):
        return self.p - Fibo(self.p).aodd()

    def num(self):
        list = Fibo(self.p).list()
        return list[self.p - 1]

#Graph class is not ready yet, but if you want to use
#uncomment the class and the libray imported over the document  
'''
class Graph:
    
    def __init__(self, min, max, title, xlabel, ylabel):
       self.min = int(min)
       self.max = int(max)
       self.title = str(title)
       self.xlabel = str(xlabel)
       self.ylabel = str(ylabel)
    pass

    def Plot(self):
        dif = self.max - self.min

        y = np.zeros(dif*100)
        x = np.linspace(self.min, self.max , dif*100)

        for i in range(0, dif*100):

    # HERE YOU PUT THE FORMULA#
    #x[i] is the x of the math function#

            y[i] = 50*x[i]
        return plt.plot(x,y)

    def Config(self):
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)

    def Show(self):
        Graph(self.min, self.max, self.title, self.xlabel, self.ylabel).Plot()
        Graph(self.min, self.max,  self.title, self.xlabel, self.ylabel).Config()
        plt.show()
'''       

        
