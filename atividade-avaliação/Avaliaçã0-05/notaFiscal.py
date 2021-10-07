"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado. 
"""
import datetime
from cliente import Cliente
from produto import Produto
from itemNotaFiscal import ItemNotaFiscal

class NotaFiscal(Cliente):         
    def __init__(self, Id, codigo, cliente, cnpjcpf):
        self._cnpjcpf = cnpjcpf
        self._Id = Id
        self._codigo=codigo
        self._cliente=cliente 
        self._data=datetime.datetime.now()   
        self._itens=[]
        self._valorNota=0.0        
        
    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente=cliente    
            
    def adicionarItem(self, item): 
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)
        
    def calcularNotaFiscal(self):
        valor=0.0
        for item in self._itens:
            valor = valor + item._valorItem
        self.valorNota=valor
        
    def data_nota(self):
        lista_data_e_hora = str(self._data).split()  
        data_lista = lista_data_e_hora[0].split('-')  
        data_final_nota = f'{data_lista[2]}/{data_lista[1]}/{data_lista[0]}'  
        return data_final_nota 
     
    def linhaItem(self, item):
        linha = list()
        for notaItem in [item._sequencial, item._descricao, item._quantidade, item._valorUnitario, item._valorItem]:
            linha.append(str(notaItem))
        return linha 
    
    def imprimirNotaFiscal(self):       
        for i in range(90):
            print("-", end ="")
        print()
        print("{0}{1:>69}{2}".format("Nota Fiscal", " ", self.data_nota()))
        print("{0}{2}{1:>5}{3}{4}".format("Cliente: ", " ", self._Id, "Nome: ", self._cnpjcpf))
        print("{}{}".format("CPF/CNPJ: ", self._cnpjcpf))
        for i in range(90):
            print("-", end ="")
        print()
        print("ITENS")
        for i in range(90):
            print("-", end ="")
        print()
        print("{0:<6}{1:<40}{2:<10}{3:}{4:>15}".format("Seq", "Descrição", "QTD", "Valor Unit", "Preço"))
        for i in range(4):
            print("-", end ="")
        print("   ", end ="")
        for i in range(35):
            print("-", end ="")
        print("   ", end ="")
        for i in range(5):
            print("-", end ="")  
        print("    ", end ="")
        for i in range(15):
            print("-", end ="")   
        print("    ", end ="")
        for i in range(17):
            print("-", end ="")  
        print()
        for item in self._itens:
            print("{:4s} {:56s}      {:>3s}       {:>10s}       {:>15s}".format(*self.linhaItem(item)))
        for i in range(90):
            print("_", end ="")
        print()
        self.calcularNotaFiscal()
        print("Valor Total: " + str(self.valorNota))
        

        


