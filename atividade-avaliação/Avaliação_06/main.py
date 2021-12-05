from produto import Produto
from cliente import Cliente
from notafiscal import NotaFiscal
from itemnotafiscal import ItemNotaFiscal
from DB import db


def main():
    db.create_all()

    cl = Cliente(1, "Umberto", 111, '111.111.111-11', 1)
    db.session.add(cl)
    db.session.commit()

    nota = NotaFiscal(1, 100, 1)
    db.session.add(nota)
    db.session.commit()

    p1 = Produto(1, 100, "Arroz", 6.0)
    db.session.add(p1)
    db.session.commit()

    it1 = ItemNotaFiscal(1, 1, 10, 1, 1)
    db.session.add(it1)
    db.session.commit()

    p2 = Produto(2, 200, "Feijao", 8.23)
    db.session.add(p2)
    db.session.commit()

    it2 = ItemNotaFiscal(2, 2, 10, 2, 1)
    db.session.add(it2)
    db.session.commit()

    p3 = Produto(3, 300, "Macarao", 6.55)
    db.session.add(p3)
    db.session.commit()

    it3 = ItemNotaFiscal(3, 3, 10, 3, 1)
    db.session.add(it3)
    db.session.commit()

    nota.imprimirNotaFiscal()


if __name__ == '__main__':
    main()
