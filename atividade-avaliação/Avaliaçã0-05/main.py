from produto        import Produto
from cliente        import Cliente
from notaFiscal     import NotaFiscal
from itemNotaFiscal import ItemNotaFiscal
from tipoCliente    import TipoCliente
 
cliente=Cliente(1, "Umberto", 111, "111.111.111-11", 1)
    
p1=Produto(1,100,"Arroz Agulha", 5.5) 
it1=ItemNotaFiscal(1, 1, 10, p1)
    
p2=Produto(2,200,"Feijão Mulatinho", 8.5) 
it2=ItemNotaFiscal(2, 2, 10, p2)
    
p3=Produto(3,300,"Macarrão Fortaleza", 4.5) 
it3=ItemNotaFiscal(3, 3, 10, p3)
    
nota = NotaFiscal(1,100,cliente, "123456789")
    
nota.adicionarItem(it1)  
nota.adicionarItem(it2)   
nota.adicionarItem(it3)
    
nota.calcularNotaFiscal()
    
nota.imprimirNotaFiscal()


