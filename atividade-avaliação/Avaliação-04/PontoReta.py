"""Escreva em Python uma classe Ponto que possui os atributos inteiros x e y. 
Escreva uma classe Reta que possui dois pontos a e b. 
Escreva os métodos construtores para a classe Ponto e para a Classe Reta. 
Escreva os métodos get e set para acessar e alterar os atributos da classe Ponto e da classe Reta. 
Escreva um método distancia que retorna um valor real da distancia entre os dois pontos da reta."""

class Ponto:
    def __init__(self, x, y):
        self.__x = int(x)
        self.__y = int(y)
        
    def set_x(self, x):
        self.__x = x
    
    def get_x(self):
        return self.__x
    
    def set_y(self, y):
        self.__y = y
    
    def get_y(self):
        return self.__y
    
class Reta:
    def __init__(self, pontoA, pontoB):
        self.pontoA = pontoA
        self.pontoB = pontoB
        
    def set_pontoA(self, pontoA):
        self.pontoA = pontoA.Ponto()
    
    def get_pontoA(self):
        return self.pontoA.Ponto()
    
    def set_pontoB(self, pontoB):
        self.pontoB = pontoB.Ponto()
    
    def get_pontoB(self):
        return self.pontoB.Ponto()
    
    def distancia(self):
        d = ()
    
    
    