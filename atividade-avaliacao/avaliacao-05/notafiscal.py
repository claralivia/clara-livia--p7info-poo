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
from datetime       import date, datetime
from cliente        import Cliente
from produto        import Produto
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal():         
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo=codigo
        self._cliente=cliente 
        self._date = datetime.today()
        self._data = self._date.strftime('%d/%m/%Y')
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
        print('----   -------------------------------------------------   -----   -----------------   -----------------')
        for c in range(0, 3):
            print('{0:<8}{1:<40}{2:>15}{3:>20}{4:>20}'.format(self._itens[c].getSequencial(),  self._itens[c].getDescricao(), self._itens[c].getQuantidade(), self._itens[c].getValorUnitario(), self._itens[c].getValorItem()))
        separar(104)
        print('\nValor Total:', self.valorNota)
        separar(104)
    
    