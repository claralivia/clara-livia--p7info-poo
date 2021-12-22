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
from cliente        import Cliente
from tipocliente import TipoCliente
from datetime       import date
from itemnotafiscal import ItemNotaFiscal
from BANCO import bancodados


class NotaFiscal(bancodados.Model):
    __tablename__ = 'TB_NOTA_FISCAL'
    id = bancodados.Column(bancodados.Integer, primary_key=True)
    codigo = bancodados.Column(bancodados.Integer, nullable=False)
    clienteID = bancodados.Column(bancodados.Integer, bancodados.ForeignKey("TB_CLIENTE.id"), nullable=False)
    data = bancodados.Column(bancodados.String, nullable=False)
    itens = bancodados.relationship("ItemNotaFiscal", backref="NotaFiscal", lazy=True)

    def __init__(self, Id, codigo, cliente):
        super().__init__(id=id, codigo=codigo, clienteID=clienteID, data=date.strftime('%d/%m/%Y'))
        
    def calcularNotaFiscal(self):
        valor = 0
        for item in self.itens:
            valor = valor + item.valorItem
        self.valorNota=valor
    def getCliente(self):
        clientePesquisa = Cliente.query.filter_by(id=self.clienteID)
        cliente = dict()
        cliente["nome"] = clientePesquisa[0].nome
        cliente["codigo"] = clientePesquisa[0].codigo
        cliente["cnpjcpf"] = clientePesquisa[0].cnpjcpf
        cliente["tipo"] = TipoCliente(clientePesquisa[0].tipo) 
        return cliente

    def imprimirNotaFiscal(self):
        def separar(num):
            for i in range(0, num):
                print('-', end='')

        separar(104)
        print('\n{0:<46}{1:>47}'.format('NOTA FISCAL', ' '), end=' ')
        print(f'{self._data}')
        print(f'Cliente: {self._cliente._codigo}\t Nome: {self._cliente._nome}')
        print(f'CPF/CNPJ: {self._cliente._cnpjcpf}')
        separar(104)
        print('\nITEMS')
        separar(104)
        print('\n{0:<8}{1:<40}{2:>15}{3:>20}{4:^22}'.format('Seq', 'Descrição', 'QTD', 'Valor Unit', 'Preço'))
        print(
            '----   -------------------------------------------------   -----   -----------------   -----------------')
        for c in range(0, 3):
            print('{0:<8}{1:<40}{2:>15}{3:>20}{4:>20}'.format(self._itens[c].getSequencial(),
                                                              self._itens[c].getDescricao(),
                                                              self._itens[c].getQuantidade(),
                                                              self._itens[c].getValorUnitario(),
                                                              self._itens[c].getValorItem()))
        separar(104)
        print('\nValor Total:', self.valorNota)
        separar(104)