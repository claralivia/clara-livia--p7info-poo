"""
  Módulo main - instancia objetos de classes definidas em
                módulos do pacote projeto01.   
"""
from produto        import Produto
from cliente        import Cliente
from notafiscal     import NotaFiscal
from itemnotafiscal import ItemNotaFiscal
from DB import db


def main():

    db.create_all()
    
    p1 = Produto(1, 100, "Arroz Agulha", 5.5)
    db.session.add(p1)
    db.session.commit()

    it1 = ItemNotaFiscal(1, 1, 10, 1, 1)
    db.session.add(it1)
    db.session.commit()


    p2 = Produto(2, 200, "Feijao Mulatinho", 8.5)
    db.session.add(p2)
    db.session.commit()

    it2 = ItemNotaFiscal(2, 2, 10, 2, 1)
    db.session.add(it2)
    db.session.commit()


    p3 = Produto(3, 300, "Macarao Fortaleza", 4.5)
    db.session.add(p3)
    db.session.commit()

    it3 = ItemNotaFiscal(3, 3, 10, 3, 1)
    db.session.add(it3)
    db.session.commit()
    
    nf.imprimirNotaFiscal()


if __name__ == '__main__':
    main()


