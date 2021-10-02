"""
1) Criar uma Pilha Vazia;
2) Inserir um elemento na Pilha (a inserção é pelo topo da Pilha);
3) Retirar um elemento da Pilha (a retirada é pelo topo da Pilha);  
4) Mostrar a Pilha.
"""

class Pilha():
    
    def __init__(self):
       self.pilha = []
       
    def adicionar(self, elemento):
       self.pilha.append(elemento)
    
    def retirar(self):
        if len(self.pilha) > 0:
            return self.pilha.pop(-1)
    
    def vazio(self):
        return self.pilha == []
    
    def mostrarPilha(self):
        print(self.pilha)
       
    
stack = Pilha()

for i in range(10):
    stack.adicionar(i)

stack.mostrarPilha()
stack.retirar()
stack.mostrarPilha()

for i in range(10):
    stack.retirar()

stack.mostrarPilha()