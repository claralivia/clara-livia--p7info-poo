"""
  Módulo main - instancia objetos de classes definidas em
                módulos do pacote projeto01.   
"""
from produto        import Produto
from cliente        import Cliente
from notafiscal import NotaFiscal
from itemnotafiscal import ItemNotaFiscal
from BANCO import bancodados


def main():

    bancodados.create_all()

    cli = Cliente(1, "Jose Maria", 100, "200.100.345-34", 1)
    bancodados.session.add(cli)
    bancodados.session.commit()

    nf = NotaFiscal(1, 100, 1)
    bancodados.session.add(nf)
    bancodados.session.commit()
    
    p1 = Produto(1, 100, "Arroz Agulha", 5.5)
    bancodados.session.add(p1)
    bancodados.session.commit()

    it1 = ItemNotaFiscal(1, 1, 10, 1, 1)
    bancodados.session.add(it1)
    bancodados.session.commit()


    p2 = Produto(2, 200, "Feijao Mulatinho", 8.5)
    bancodados.session.add(p2)
    bancodados.session.commit()

    it2 = ItemNotaFiscal(2, 2, 10, 2, 1)
    bancodados.session.add(it2)
    bancodados.session.commit()


    p3 = Produto(3, 300, "Macarao Fortaleza", 4.5)
    bancodados.session.add(p3)
    bancodados.session.commit()

    it3 = ItemNotaFiscal(3, 3, 10, 3, 1)
    bancodados.session.add(it3)
    bancodados.session.commit()

    nf.imprimirNotaFiscal()


if __name__ == '__main__':
    main()


