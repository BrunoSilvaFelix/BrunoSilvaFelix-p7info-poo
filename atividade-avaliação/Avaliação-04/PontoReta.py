
class Ponto():
    def __init__(self, x , y):
        self.x = x
        self.y = y
    
    def set_X(self, x):
        self.x = x
    
    def set_Y(self, y):
        self.y = y
    
    def get_X(self):
        return self.x

    def get_Y(self):
        return self.y

class Reta():
    def __init__(self, pontoA, pontoB):
        self.pontoA = pontoA
        self.pontoB = pontoB

    def set_pontoA(self, pontoA):
        self.pontoA = pontoA

    def set_pontoB(self, pontoB):
        self.pontoB = pontoB
    
    def get_pontoA(self):
        return self.pontoA
    
    def get_pontoB(self):
        return self.pontoB

    def distancia(self):
        parteX = (self.get_pontoB().get_X() - self.get_pontoA().get_X())**2
        parteY = (self.get_pontoB().get_Y() - self.get_pontoA().get_Y())**2
        resultado = (parteX + parteY) ** 0.5
        
        return resultado


pontoA = Ponto(0, 0)
pontoB = Ponto(3, 4)

retaA = Reta(pontoA,pontoB)

print("A distância entre os pontos A e B é", retaA.distancia())

