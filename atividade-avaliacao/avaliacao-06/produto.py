"""
    Módulo produto
    Classe Produto
    Atributos :
        id            - informado
        codigo        - informado
        descricao     - informado
        valorUnitario - informado. 
"""

from BANCO import bancodados

class Produto(bancodados.Model):
    __tablename__ = 'TB_PRODUTO'
    id = bancodados.Column(bancodados.Integer, primary_key=True)
    codigo = bancodados.Column(bancodados.Integer, nullable=False)
    descricao = bancodados.Column(bancodados.String, nullable=False)
    valorUnitario = bancodados.Column(bancodados.Float, nullable=False)

    def __init__(self, id, codigo, descricao, valorUnitario):
        super().__init__(id=id, codigo=codigo, descricao=descricao, valorUnitario=valorUnitario)
        
    def getDescricao(self):
        return self._descricao
    
    def getValorUnitario(self): 
        return self._valorUnitario
        
    def str(self):
        string="\nId={3} Codigo={2} Descricao={1} Valor Unitario={0}".format(self._valorUnitario, self._descricao, self._codigo, self._id)
        return string
    
   
    
if __name__ == '__main__':
    produto = Produto(id=1, codigo=100, descricao="Arroz Agulha", valorUnitario=5.5)
    print(produto.str())
    bancodados.session.add(produto)
    bancodados.session.commit()
        
        
