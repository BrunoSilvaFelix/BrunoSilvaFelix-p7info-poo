"""
Implemente em Python a Estrutura de Dados Fila (FIFO - FIRST IN FIRST OUT). 
Use uma Lista para implementar em Python.
As Operações em uma Fila são:
1) Criar uma Fila Vazia;
2) Inserir um elemento na Fila (a inserção é feita no fim da Fila);
3) Retirar um elemento da Fila (a retirada é feita no inicio da da Fila);  
4) Mostrar a Fila.
"""

class Fila():
    
    def __init__(self):
        self.fila = []
        
    def inserir(self, elemento):
        self.fila.append(elemento)
        
    def retirar(self):
        if len(self.fila) > 0:
            del self.fila[0]
    
    def vazia(self):
        return self.fila == []
    
    def mostrarFila(self):
        print (self.fila)
        
queue = Fila()

for i in range(3):
    queue.inserir(i)
    
queue.mostrarFila()
queue.inserir(3)
queue.mostrarFila()
queue.retirar()
queue.mostrarFila()

for i in range(5):
    queue.retirar()

queue.mostrarFila()