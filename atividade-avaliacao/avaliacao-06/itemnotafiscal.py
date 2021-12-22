"""
    Módulo itemnotafiscal 
    Classe ItemNotaFiscal 
    Atributos :
        id         - informado
        sequencial - informado
        quantidade - informado
        produto    - informado
        valor      - calculado.            
"""
from produto import Produto
from BANCO import bancodados

class ItemNotaFiscal(bancodados.Model):
    __tablename__ = 'TB_ITEM_NF'
    id = bancodados.Column(bancodados.Integer, primary_key=True)
    sequencial = bancodados.Column(bancodados.Integer, nullable=False)
    quantidade = bancodados.Column(bancodados.Integer, nullable=False)
    produtoID = bancodados.Column(bancodados.Integer, bancodados.ForeignKey("TB_PRODUTO.id"), nullable=False)
    NotaFiscalID = bancodados.Column(bancodados.Integer, bancodados.ForeignKey("TB_NOTA_FISCAL.id"), nullable=False)
  
    def __init__(self, id, sequencial, quantidade, produto):
        super().__init__(id=id, sequencial=sequencial,
                         quantidade=quantidade, produtoID=produtoID,
                         NotaFiscalID=NotaFiscalID)
        produto = Produto.query.filter_by(id=self.produtoID)
        self.descricao = produto[0].descricao
        self.valorUnitario = produto[0].valorUnitario
        self.valorItem = self.quantidade * self.valorUnitario
      
    def str(self):
        string="\nId={5} Sequencial={4} Quantidade={3} Produto={2} Valor Unitario={1} Valor Item={0}".format(self._valorItem,
                                                                                                             self._valorUnitario,
                                                                                                             self._descricao, 
                                                                                                             self._quantidade, 
                                                                                                             self._sequencial, 
                                                                                                             self._id)
        return string
    
        
if __name__ == '__main__':
    it1=ItemNotaFiscal(1, 1, 10, 1, 0)
    print(it1.str())
