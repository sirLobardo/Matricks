# Matricks
# Coded By sirLobardo

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
        
